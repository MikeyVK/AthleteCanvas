#!/usr/bin/env python3
"""
Transcript Extractor Script voor Ypsia / Antigravity

Zet Antigravity JSONL-transcripts om naar een schone, menselijk leesbare Markdown-weergave.
Ondersteunt geavanceerde filtering op tijdsintervallen, stap-indices en inhoudstypes.

Gebruik:
    python scripts/extract_transcript.py [opties]

Voorbeelden:
    # Standaard extractie van de huidige conversatie
    python scripts/extract_transcript.py

    # Exporteer naar een specifiek bestand met een tijdsfilter
    python scripts/extract_transcript.py --start-time "2026-08-01T20:00:00" -o docs/gesprek_aug1.md

    # Exporteer uitsluitend de stappen tussen index 1500 en 1600 zonder denkstappen
    python scripts/extract_transcript.py --start-step 1500 --end-step 1600 --no-thinking
"""

import argparse
import datetime
import json
import os
import sys

DEFAULT_TRANSCRIPT = r"C:\Users\miche\.gemini\antigravity\brain\0ff47fb1-bd71-4157-af0f-011b96af6c1c\.system_generated\logs\transcript.jsonl"

def parse_iso_time(ts_str):
    if not ts_str:
        return None
    try:
        ts_clean = ts_str.replace("Z", "+00:00")
        return datetime.datetime.fromisoformat(ts_clean)
    except Exception as e:
        print(f"Waarschuwing: kon datum '{ts_str}' niet parsen: {e}")
        return None

def extract_transcript(args):
    input_path = args.input or DEFAULT_TRANSCRIPT
    if not os.path.exists(input_path):
        print(f"Fout: Invoerbestand niet gevonden op: {input_path}")
        sys.exit(1)

    output_path = args.output
    if not output_path:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}_extracted.md"

    start_dt = parse_iso_time(args.start_time)
    end_dt = parse_iso_time(args.end_time)

    lines_processed = 0
    items_matched = 0

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"# Conversatie Extractie ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})\n\n")
        outfile.write(f"*Bron: `{input_path}`*\n\n---\n\n")

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

            # 1. Gebruikersinvoer
            if (step_type == "USER_INPUT" or source == "USER_EXPLICIT") and args.include_user:
                items_matched += 1
                outfile.write(f"## 👤 Gebruiker [Stap {step_idx} | {created_at}]\n\n")
                outfile.write(f"{content.strip()}\n\n")
                outfile.write("---\n\n")

            # 2. Model antwoorden & Redeneerstappen
            elif step_type == "PLANNER_RESPONSE" or source == "MODEL":
                wrote_section = False

                # Denkstappen
                if args.include_thinking and thinking and thinking.strip():
                    items_matched += 1
                    wrote_section = True
                    outfile.write(f"### 💭 Redenering (Thinking) [Stap {step_idx}]\n\n")
                    quoted = "\n".join([f"> {l}" for l in thinking.strip().split("\n")])
                    outfile.write(f"{quoted}\n\n")

                # Inhoudelijk antwoord
                if args.include_assistant and content and content.strip():
                    items_matched += 1
                    wrote_section = True
                    outfile.write(f"## 🤖 Antigravity [Stap {step_idx} | {created_at}]\n\n")
                    outfile.write(f"{content.strip()}\n\n")

                if wrote_section:
                    outfile.write("---\n\n")

            # 3. Optionele Tool-samenvatting
            elif args.include_tools and step_type in ("MCP_TOOL", "RUN_COMMAND", "SAFE_EDIT_FILE"):
                items_matched += 1
                outfile.write(f"#### 🛠️ Tool Execution [{step_type} | Stap {step_idx}]\n\n")
                summary_snippet = content.strip().split("\n")[0] if content else ""
                outfile.write(f"`{summary_snippet[:150]}`\n\n")

    print(f"✅ Extractie voltooid!")
    print(f"- Regels verwerkt: {lines_processed}")
    print(f"- Elementen geëxtraheerd: {items_matched}")
    print(f"- Uitvoerlocatie: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Parset en filtert Antigravity JSONL-transcripts naar schone Markdown."
    )
    parser.add_argument("-i", "--input", help="Pad naar het invoer JSONL transcript bestand.")
    parser.add_argument("-o", "--output", help="Pad waar het Markdown bestand opgeslagen moet worden.")
    
    # Filter opties
    parser.add_argument("--start-time", help="Starttijd in ISO formaat (bijv. '2026-08-01T20:00:00').")
    parser.add_argument("--end-time", help="Eindtijd in ISO formaat (bijv. '2026-08-02T12:00:00').")
    parser.add_argument("--start-step", type=int, help="Minimale stap-index (step_index).")
    parser.add_argument("--end-step", type=int, help="Maximale stap-index (step_index).")

    # Inhoud schakelaars
    parser.add_argument("--no-thinking", dest="include_thinking", action="store_false", help="Sluit denkstappen (thinking) uit.")
    parser.add_argument("--no-user", dest="include_user", action="store_false", help="Sluit gebruikersberichten uit.")
    parser.add_argument("--no-assistant", dest="include_assistant", action="store_false", help="Sluit assistent-antwoorden uit.")
    parser.add_argument("--include-tools", action="store_true", help="Voeg een beknopte samenvatting van tool-uitvoeringen toe.")

    parser.set_defaults(include_thinking=True, include_user=True, include_assistant=True)

    args = parser.parse_args()
    extract_transcript(args)

if __name__ == "__main__":
    main()
