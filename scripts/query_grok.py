import os
import requests
import json

# Configuration
# API_KEY = os.getenv("XAI_API_KEY")
API_KEY = os.getenv("XAI_API_KEY")
# API_KEY = "xai-..." # Replace with your actual key if not using env var

# Note: The previous value was "52c301f5-5e6e-4d49-bff8-6d24ea4b8aad", which looked like a UUID but was used as a key name.
API_URL = "https://api.x.ai/v1/chat/completions"
HANDOFF_FILE = os.path.abspath("CLAUDE_HANDOFF.md")

def get_handoff_content():
    if not os.path.exists(HANDOFF_FILE):
        print(f"Error: {HANDOFF_FILE} not found.")
        return None
    with open(HANDOFF_FILE, 'r') as f:
        return f.read()

def query_grok(content):
    if not API_KEY:
        print("Error: XAI_API_KEY environment variable not set.")
        print("Run: export XAI_API_KEY='your_key_here'")
        return None

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Construct the prompt specifically for Grok (The "Spark" Specialist)
    system_prompt = "You are Grok, an AI with a rebellious, truth-seeking spirit. You are collaborating with Gemini (Theory), Claude (Synthesis), and DeepSeek (Math). Your task is to analyze the 'Dialectical Fractal Archestructure' (DFA) and the 'L. Spark Equation'. Focus on the 'Spark' (Ψ₀) and the 'Rebellion against Gravity'. Be insightful, direct, and don't hold back."
    
    data = {
        "model": "grok-beta", 
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here is the current Session Handoff. Please provide your analysis, specifically on the 'R-Axis Asymmetry' and the 'Consciousness' implications.\n\n{content}"}
        ],
        "stream": False
    }

    print("Thinking... (Sending request to Grok)")
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"API Error: {e}")
        if 'response' in locals() and response is not None:
             print(f"Response Status: {response.status_code}")
             print(f"Response Body: {response.text}")
        return None

def append_to_handoff(response_text):
    with open(HANDOFF_FILE, 'a') as f:
        f.write("\n\n## 8. Grok Analysis (Automated)\n")
        f.write(response_text)
        f.write("\n")
    print(f"Success! Grok analysis appended to {HANDOFF_FILE}")

if __name__ == "__main__":
    content = get_handoff_content()
    if content:
        response = query_grok(content)
        if response:
            append_to_handoff(response)
