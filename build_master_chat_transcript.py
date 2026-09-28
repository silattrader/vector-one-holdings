#!/usr/bin/env python3
"""
Master Chat Transcript Builder for Vector One Holdings
Extracts all conversation turns across all past JSONL transcripts and current session logs
and formats them into VECTOR_ONE_MASTER_CHAT_TRANSCRIPT.md.
"""

import json
import os
import re

OUTPUT_MD_PATH = r"c:\Users\User\Desktop\Vector One\Vector_One_Outputs\VECTOR_ONE_MASTER_CHAT_TRANSCRIPT.md"

TRANSCRIPT_SOURCES = [
    r"c:\Users\User\Desktop\Vector One\Vector_One_Chat_History.jsonl",
    r"c:\Users\User\Desktop\Vector One\Vector_One_Outputs\chat_transcript.jsonl",
    r"C:\Users\User\.gemini\antigravity-ide\brain\8e8a340b-1104-4df2-aa94-8d718c633a4e\.system_generated\logs\transcript.jsonl"
]

def clean_user_content(content):
    if not content:
        return ""
    # Strip <USER_REQUEST> tags if present
    match = re.search(r'<USER_REQUEST>\s*(.*?)\s*</USER_REQUEST>', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Strip metadata blocks
    content = re.sub(r'<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>', '', content, flags=re.DOTALL)
    content = re.sub(r'<USER_SETTINGS_CHANGE>.*?</USER_SETTINGS_CHANGE>', '', content, flags=re.DOTALL)
    return content.strip()

def extract_transcript_entries(file_path):
    entries = []
    if not os.path.exists(file_path):
        return entries
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                source = data.get("source", "")
                type_ = data.get("type", "")
                created_at = data.get("created_at", "")
                content = data.get("content", "")

                if type_ == "USER_INPUT" and source == "USER_EXPLICIT":
                    clean_txt = clean_user_content(content)
                    if clean_txt:
                        entries.append({
                            "role": "USER",
                            "timestamp": created_at,
                            "content": clean_txt
                        })
                elif type_ == "PLANNER_RESPONSE" and source == "MODEL":
                    # Extract thinking or tool call summary if any
                    thinking = data.get("thinking", "").strip()
                    tool_calls = data.get("tool_calls", [])
                    
                    text_parts = []
                    if thinking:
                        text_parts.append(f"**Thinking / Strategy:**\n{thinking}")
                    if tool_calls:
                        call_names = [tc.get("name", "") for tc in tool_calls]
                        text_parts.append(f"**Executed Actions / Tools:** `{', '.join(call_names)}`")
                    if content:
                        text_parts.append(content.strip())
                    
                    full_resp = "\n\n".join(text_parts).strip()
                    if full_resp:
                        entries.append({
                            "role": "ASSISTANT",
                            "timestamp": created_at,
                            "content": full_resp
                        })
            except Exception as e:
                continue
    return entries

def main():
    all_entries = []
    seen_user_prompts = set()

    for src in TRANSCRIPT_SOURCES:
        entries = extract_transcript_entries(src)
        for entry in entries:
            # Deduplicate repeated identical user entries across logs
            if entry["role"] == "USER":
                key = (entry["timestamp"], entry["content"])
                if key in seen_user_prompts:
                    continue
                seen_user_prompts.add(key)
            all_entries.append(entry)

    # Write Master Markdown File
    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as out:
        out.write("# 💬 Vector One Holdings — Master Conversation & Chat Log\n\n")
        out.write("**Entity:** Vector One Holdings / Vector Systems Group  \n")
        out.write("**Repository:** [silattrader/vector-one-holdings](https://github.com/silattrader/vector-one-holdings)  \n")
        out.write("**Purpose:** Dedicated chronological markdown transcript of all chat interactions, instructions, decisions, and system outputs.\n\n")
        out.write("---\n\n")

        session_count = 1
        current_role = None

        for entry in all_entries:
            role = entry["role"]
            ts = entry["timestamp"]
            text = entry["content"]

            if role == "USER":
                out.write(f"\n### 👤 USER ({ts})\n\n")
                out.write(f"> {text.replace('\n', '\n> ')}\n\n")
            elif role == "ASSISTANT":
                out.write(f"### 🤖 ANTIGRAVITY AI ASSISTANT ({ts})\n\n")
                out.write(f"{text}\n\n")
                out.write("---\n")

    print(f"[SUCCESS] Master Chat Transcript generated at: {OUTPUT_MD_PATH}")

if __name__ == "__main__":
    main()
