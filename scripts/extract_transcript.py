#!/usr/bin/env python3
"""
Pure Dialogue Extractor Script voor Ypsia / Antigravity

Zet Antigravity JSONL-transcripts om naar een puur taalkundig dialoogbestand.
Verwijdert ALLE codeblokken, documentdumps, tool-outputs en systeemruis.

Doel:
    Een vederlicht, puur tekstueel transcript dat alleen onze inhoudelijke
    conversatie en redeneerstappen bevat, ideaal voor menselijke lezing en
    het inlezen door (externe) AI-agents.

Gebruik:
    python scripts/extract_transcript.py [opties]

Voorbeelden:
    python scripts/extract_transcript.py -o .pgmcp/logs/pure_dialogue.md
    python scripts/extract_transcript.py --no-thinking -o .pgmcp/logs/pure_dialogue.md
"""

import argparse
import datetime
import json
import os
import re
import sys

DEFAULT_TRANSCRIPT = r"C:\Users\miche\.gemini\antigravity\brain\0ff47fb1-bd71-4157-af0f-011b96af6c1c\.system_generated\logs\transcript_full.jsonl"

def parse_iso_time(ts_str):
    if not ts_str:
        return None
    try:
        ts_clean = ts_str.replace("Z", "+00:00")
        return datetime.datetime.fromisoformat(ts_clean)
    except Exception as e:
        return None

def format_short_time(ts_str):
    """Formatteer een ISO datumstring naar YYYY-MM-DD HH:MM:SS."""
    dt = parse_iso_time(ts_str)
    if dt:
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    return ts_str or ""

def strip_non_dialogue(text):
    """
    Verwijder alle codeblokken, documentdumps en systeem-metadata.
    Behoud uitsluitend de zuivere taalkundige dialoog.
    """
    if not text:
        return ""

    # 1. Strip omheinde codeblokken (```...```)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)

    # 2. Strip systeem- en XML-tags
    text = re.sub(r'<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>', '', text, flags=re.DOTALL)
    text = re.sub(r'<user_information>.*?</user_information>', '', text, flags=re.DOTALL)
    text = re.sub(r'<SYSTEM_MESSAGE>.*?</SYSTEM_MESSAGE>', '', text, flags=re.DOTALL)
    text = re.sub(r'<user_rules>.*?</user_rules>', '', text, flags=re.DOTALL)
    text = re.sub(r'<workflows>.*?</workflows>', '', text, flags=re.DOTALL)
    text = re.sub(r'<skills>.*?</skills>', '', text, flags=re.DOTALL)
    text = re.sub(r'<subagents>.*?</subagents>', '', text, flags=re.DOTALL)
    text = re.sub(r'<messaging>.*?</messaging>', '', text, flags=re.DOTALL)
    text = re.sub(r'<artifacts>.*?</artifacts>', '', text, flags=re.DOTALL)

    # 3. Strip eventuele losse file-dump patronen (zoals view_file outputs)
    text = re.sub(r'File Path: `file:///.*?`(\n.*?)?(?=^\s*#|^\s*##|\Z)', '', text, flags=re.DOTALL | re.MULTILINE)
    text = re.sub(r'^Created At:.*?\n(Completed At:.*?\n)?', '', text, flags=re.DOTALL)

    # 4. Opschonen van witregels
    lines = [line.rstrip() for line in text.splitlines()]
    clean_lines = []
    prev_empty = False
    for line in lines:
        if not line:
            if not prev_empty:
                clean_lines.append("")
                prev_empty = True
        else:
            clean_lines.append(line)
            prev_empty = False

    return "\n".join(clean_lines).strip()

def extract_pure_dialogue(args):
    input_path = args.input or DEFAULT_TRANSCRIPT
    if not os.path.exists(input_path):
        fallback = input_path.replace("transcript_full.jsonl", "transcript.jsonl")
        if os.path.exists(fallback):
            input_path = fallback
        else:
            print(f"Fout: Invoerbestand niet gevonden op: {input_path}")
            sys.exit(1)

    output_path = args.output or r".pgmcp\logs\pure_dialogue.md"

    start_dt = parse_iso_time(args.start_time)
    end_dt = parse_iso_time(args.end_time)

    lines_processed = 0
    items_matched = 0

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"# Puur Taalkundig Dialoog Transcript\n\n")
        outfile.write(f"*Gegenereerd op: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Bron: `{input_path}`*\n\n---\n\n")

        for line in infile:
            lines_processed += 1
            line = line.strip()
            if not line:
                continue

            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            step_idx = data.get("step_index")
            created_at = data.get("created_at", "")
            event_dt = parse_iso_time(created_at)

            # Filter 1: Stap indexen
            if args.start_step is not None and step_idx is not None and step_idx < args.start_step:
                continue
            if args.end_step is not None and step_idx is not None and step_idx > args.end_step:
                continue

            # Filter 2: Tijdsinterval
            if start_dt and event_dt and event_dt < start_dt:
                continue
            if end_dt and event_dt and event_dt > end_dt:
                continue

            step_type = data.get("type", "")
            source = data.get("source", "")
            content = data.get("content", "")
            thinking = data.get("thinking", "")
            short_ts = format_short_time(created_at)

            meta_str = f" [{short_ts}]" if args.include_metadata else ""

            # 1. Gebruikersinvoer
            if (step_type == "USER_INPUT" or source == "USER_EXPLICIT") and args.include_user:
                cleaned_user = strip_non_dialogue(content)
                if cleaned_user:
                    items_matched += 1
                    outfile.write(f"## 👤 Gebruiker{meta_str}\n\n")
                    outfile.write(f"{cleaned_user}\n\n")
                    outfile.write("---\n\n")

            # 2. Model antwoorden & Redeneerstappen (ALLEEN van PLANNER_RESPONSE, nooit MCP_TOOL of VIEW_FILE outputs!)
            elif step_type == "PLANNER_RESPONSE":
                wrote_section = False

                # Denkstappen
                cleaned_thinking = strip_non_dialogue(thinking)
                if args.include_thinking and cleaned_thinking:
                    items_matched += 1
                    wrote_section = True
                    outfile.write(f"### 💭 Redenering (Thinking){meta_str}\n\n")
                    quoted = "\n".join([f"> {l}" for l in cleaned_thinking.split("\n")])
                    outfile.write(f"{quoted}\n\n")

                # Inhoudelijk antwoord (geschreven door het model naar de gebruiker)
                cleaned_assistant = strip_non_dialogue(content)
                if args.include_assistant and cleaned_assistant:
                    items_matched += 1
                    wrote_section = True
                    outfile.write(f"## 🤖 Antigravity{meta_str}\n\n")
                    outfile.write(f"{cleaned_assistant}\n\n")

                if wrote_section:
                    outfile.write("---\n\n")

            # Negeer expliciet alle MCP_TOOL, VIEW_FILE, RUN_COMMAND, LIST_DIRECTORY stappen!

    print("[SUCCESS] Pure dialoog-extractie voltooid!")
    print(f"- Regels verwerkt: {lines_processed}")
    print(f"- Dialoog-interacties ge-extraheerd: {items_matched}")
    print(f"- Uitvoerlocatie: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Extracteert uitsluitend de puur taalkundige dialoog uit Antigravity JSONL-transcripts."
    )
    parser.add_argument("-i", "--input", help="Pad naar het invoer JSONL transcript bestand.")
    parser.add_argument("-o", "--output", help="Pad waar het Markdown bestand opgeslagen moet worden.")
    
    parser.add_argument("--start-time", help="Starttijd in ISO formaat (bijv. '2026-08-01T20:00:00').")
    parser.add_argument("--end-time", help="Eindtijd in ISO formaat (bijv. '2026-08-02T12:00:00').")
    parser.add_argument("--start-step", type=int, help="Minimale stap-index (step_index).")
    parser.add_argument("--end-step", type=int, help="Maximale stap-index (step_index).")

    parser.add_argument("--no-thinking", dest="include_thinking", action="store_false", help="Sluit denkstappen (thinking) uit.")
    parser.add_argument("--no-user", dest="include_user", action="store_false", help="Sluit gebruikersberichten uit.")
    parser.add_argument("--no-assistant", dest="include_assistant", action="store_false", help="Sluit assistent-antwoorden uit.")
    parser.add_argument("--no-metadata", dest="include_metadata", action="store_false", help="Sluit tijdstempels in de headers uit.")

    parser.set_defaults(include_thinking=True, include_user=True, include_assistant=True, include_metadata=True)

    args = parser.parse_args()
    extract_pure_dialogue(args)

if __name__ == "__main__":
    main()
