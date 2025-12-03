import json
import time
import os
import requests
from pathlib import Path

class CycleManager:
    def __init__(self, max_responses=30):
        self.max_responses = max_responses
        self.response_count = 0
        self.active_ai = "ollama" # Defaulting to local for now
        self.ai_rotation = ["ollama"] # Add others when configured
        self.workspace = Path("/home/king/Downloads/documentsforgi/workspace")
        self.mcp_gateway_url = "http://localhost:3000" # Docker MCP Gateway

    def on_response(self, ai_name: str, response: str):
        """Called after each AI response"""
        self.response_count += 1

        # Log response
        log_file = self.workspace / "logs" / f"{ai_name}_session.log"
        with open(log_file, "a") as f:
            f.write(f"[{time.isoformat()}] {response[:500]}...\n")

        # Check trigger
        if self.response_count >= self.max_responses:
            self.trigger_clear_cycle()

    def trigger_clear_cycle(self):
        """Execute the clear and inject cycle"""
        print(f"⚡ Triggering clear cycle for {self.active_ai}")

        # 1. Have extractor AI summarize state (Mocking for now)
        state = self.extract_state(self.active_ai)

        # 2. Save state
        state_file = self.workspace / "state" / "extracted_state.json"
        with open(state_file, "w") as f:
            json.dump(state, f, indent=2)

        # 3. Clear target AI context (Would be an API call to the router/provider)
        # self.clear_context(self.active_ai)

        # 4. Inject state into fresh AI
        # self.inject_state(self.active_ai, state)

        # 5. Reset counter
        self.response_count = 0
        print(f"🔄 Cycle complete. State saved.")

    def extract_state(self, ai_name: str) -> dict:
        """Mock state extraction"""
        return {
            "timestamp": time.isoformat(),
            "source_ai": ai_name,
            "conclusions": ["Mock conclusion 1", "Mock conclusion 2"],
            "hypothesis": "Current working hypothesis..."
        }

if __name__ == "__main__":
    # Test run
    manager = CycleManager(max_responses=3)
    print("🚀 Starting Cycle Manager Test...")
    for i in range(4):
        print(f"Simulating response {i+1}...")
        manager.on_response("ollama", "This is a test response from the AI model.")
        time.sleep(0.5)
