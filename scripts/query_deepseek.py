import os
import requests
import json

# Configuration
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"
HANDOFF_FILE = os.path.abspath("CLAUDE_HANDOFF.md")

def get_handoff_content():
    if not os.path.exists(HANDOFF_FILE):
        print(f"Error: {HANDOFF_FILE} not found.")
        return None
    with open(HANDOFF_FILE, 'r') as f:
        return f.read()

def query_deepseek(content):
    if not API_KEY:
        print("Error: DEEPSEEK_API_KEY environment variable not set.")
        print("Run: export DEEPSEEK_API_KEY='your_key_here'")
        return None

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Construct the prompt specifically for the Math/Code analysis
    system_prompt = "You are DeepSeek, a specialist in Mathematical Physics and Code Analysis. You are collaborating with Gemini (Theory) and Claude (Synthesis). Your task is to verify the mathematical logic of the 'R-Axis Asymmetry' and the 'Selector Agent' model."
    
    data = {
        "model": "deepseek-chat", # Or deepseek-reasoner if available
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here is the current Session Handoff. Please focus on Section 6 (Request for DeepSeek) and provide your mathematical analysis.\n\n{content}"}
        ],
        "stream": False
    }

    print("Thinking... (Sending request to DeepSeek)")
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"API Error: {e}")
        if response:
            print(response.text)
        return None

def append_to_handoff(response_text):
    with open(HANDOFF_FILE, 'a') as f:
        f.write("\n\n## 7. DeepSeek Analysis (Automated)\n")
        f.write(response_text)
        f.write("\n")
    print(f"Success! DeepSeek analysis appended to {HANDOFF_FILE}")

if __name__ == "__main__":
    content = get_handoff_content()
    if content:
        response = query_deepseek(content)
        if response:
            append_to_handoff(response)
