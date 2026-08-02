#!/usr/bin/env python3
"""
Transcript Extractor Script voor Ypsia / Antigravity

Zet Antigravity JSONL-transcripts om naar een schone, menselijk leesbare Markdown-weergave.
Ondersteunt geavanceerde filtering op tijdsintervallen, stap-indices, inhoudstypes en metadata.

Gebruik:
    python scripts/extract_transcript.py [opties]

Voorbeelden:
    python scripts/extract_transcript.py -i C:\\...\\transcript_full.jsonl -o .pgmcp/logs/transcript_chat.md
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
    """Formatteer een ISO datumstring naar een korte, leesbare tijdstempel YYYY-MM-DD HH:MM:SS."""
    dt = parse_iso_time(ts_str)
    if dt:
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    return ts_str or ""

def clean_user_content(content_str):
    """Verwijder systeem-injected XML tags zoals <ADDITIONAL_METADATA> uit gebruikersprompts."""
    if not content_str:
        return ""
    cleaned = re.sub(r"<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>", "", content_str, flags=re.DOTALL)
    cleaned = re.sub(r"<user_information>.*?</user_information>", "", cleaned, flags=re.DOTALL)
    return cleaned.strip()

def clean_assistant_content(content_str):
    """Verwijder systeem-header ruis zoals 'Created At: ... Completed At: ...' uit assistant outputs."""
    if not content_str:
        return ""
    cleaned = re.sub(r"^Created At:.*?\n(Completed At:.*?\n)?", "", content_str.strip(), flags=re.DOTALL)
    return cleaned.strip()

def extract_transcript(args):
    input_path = args.input or DEFAULT_TRANSCRIPT
    if not os.path.exists(input_path):
        fallback = input_path.replace("transcript_full.jsonl", "transcript.jsonl")
        if os.path.exists(fallback):
            input_path = fallback
        else:
            print(f"Fout: Invoerbestand niet gevonden op: {input_path}")
            sys.exit(1)

    output_path = args.output or r".pgmcp\logs\transcript_chat.md"

    start_dt = parse_iso_time(args.start_time)
    end_dt = parse_iso_time(args.end_time)

    lines_processed = 0
    items_matched = 0

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"# Conversatie & Redeneergeschiedenis\n\n")
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
                cleaned_user = clean_user_content(content)
                if cleaned_user:
                    items_matched += 1
                    outfile.write(f"## 👤 Gebruiker{meta_str}\n\n")
                    outfile.write(f"{cleaned_user}\n\n")
                    outfile.write("---\n\n")

            # 2. Model antwoorden & Redeneerstappen
            elif step_type == "PLANNER_RESPONSE" or source == "MODEL":
                wrote_section = False

                # Denkstappen
                if args.include_thinking and thinking and thinking.strip():
                    items_matched += 1
                    wrote_section = True
                    outfile.write(f"### 💭 Redenering (Thinking){meta_str}\n\n")
                    quoted = "\n".join([f"> {l}" for l in thinking.strip().split("\n")])
                    outfile.write(f"{quoted}\n\n")

                # Inhoudelijk antwoord
                cleaned_assistant = clean_assistant_content(content)
                if args.include_assistant and cleaned_assistant:
                    items_matched += 1
                    wrote_section = True
                    outfile.write(f"## 🤖 Antigravity{meta_str}\n\n")
                    outfile.write(f"{cleaned_assistant}\n\n")

                if wrote_section:
                    outfile.write("---\n\n")

            # 3. Optionele Tool-samenvatting
            elif args.include_tools and step_type in ("MCP_TOOL", "RUN_COMMAND", "SAFE_EDIT_FILE"):
                items_matched += 1
                outfile.write(f"#### 🛠️ Tool Execution [{step_type}]{meta_str}\n\n")
                summary_snippet = clean_assistant_content(content).split("\n")[0] if content else ""
                outfile.write(f"`{summary_snippet[:150]}`\n\n")

    print("[SUCCESS] Extractie voltooid!")
    print(f"- Regels verwerkt: {lines_processed}")
    print(f"- Elementen ge-extraheerd: {items_matched}")
    print(f"- Uitvoerlocatie: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Parset en filtert Antigravity JSONL-transcripts naar schone Markdown."
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
    parser.add_argument("--include-tools", action="store_true", help="Voeg een beknopte samenvatting van tool-uitvoeringen toe.")

    parser.set_defaults(include_thinking=True, include_user=True, include_assistant=True, include_metadata=True)

    args = parser.parse_args()
    extract_transcript(args)

if __name__ == "__main__":
    main()
