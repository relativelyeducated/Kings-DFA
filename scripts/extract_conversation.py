import json
import os
from datetime import datetime

def extract_conversations():
    file_path = "/home/king/Downloads/documentsforgi/all-conversations/claude/export-2025-11-29/conversations.json"
    output_dir = "claims/pending/extracted_conversations"
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        print(f"Loaded {len(data)} conversations.")
        
        target_date = datetime(2025, 11, 27)
        
        for conv in data:
            created_at_str = conv.get('created_at', '')
            if created_at_str:
                # Handle ISO format variations if needed, assuming standard ISO
                try:
                    created_at = datetime.fromisoformat(created_at_str.replace('Z', '+00:00'))
                    if created_at >= target_date.replace(tzinfo=created_at.tzinfo):
                        print(f"Found conversation from {created_at}: {conv.get('name', 'Untitled')}")
                        
                        # Save to file
                        filename = f"{created_at.strftime('%Y-%m-%d')}_{conv.get('uuid', 'unknown')}.md"
                        with open(os.path.join(output_dir, filename), 'w') as out:
                            out.write(f"# {conv.get('name', 'Untitled')}\n\n")
                            out.write(f"Date: {created_at}\n\n")
                            for msg in conv.get('chat_messages', []):
                                sender = msg.get('sender', 'unknown')
                                text = msg.get('text', '')
                                out.write(f"## {sender}\n{text}\n\n")
                except ValueError as e:
                    print(f"Error parsing date {created_at_str}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_conversations()
