import os
from flask import Flask, request, render_template_string, redirect, url_for
import markdown

app = Flask(__name__)

HANDOFF_FILE = os.path.abspath("CLAUDE_HANDOFF.md")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DFA Handoff Interface</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }
        .container { display: flex; flex-direction: column; gap: 20px; }
        .preview { background: #f9f9f9; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .editor { display: flex; flex-direction: column; gap: 10px; }
        textarea { width: 100%; height: 150px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        h1 { color: #333; }
        .status { color: green; font-weight: bold; }
    </style>
</head>
    <script>
        // Auto-scroll to bottom on load
        window.onload = function() {
            window.scrollTo(0, document.body.scrollHeight);
            document.getElementById("reply-box").focus();
        };

        // Enter to submit
        document.addEventListener("DOMContentLoaded", function() {
            const textarea = document.getElementById("reply-box");
            const form = document.getElementById("reply-form");

            textarea.addEventListener("keydown", function(e) {
                if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault(); // Prevent newline
                    form.submit();
                }
            });
        });
    </script>
</head>
<body>
    <div class="container">
        <h1>DFA Handoff Interface 🚀</h1>
        <p>Current Status of <code>CLAUDE_HANDOFF.md</code></p>
        
        <div class="preview">
            {{ content | safe }}
        </div>

        <div class="editor">
            <h3>Append a Reply</h3>
            <form id="reply-form" action="/append" method="post">
                <textarea id="reply-box" name="reply" placeholder="Type your message... (Enter to Send, Shift+Enter for newline)"></textarea>
                <button type="submit">Send to Agents</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    if not os.path.exists(HANDOFF_FILE):
        return "Error: CLAUDE_HANDOFF.md not found!"
    
    with open(HANDOFF_FILE, 'r') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    return render_template_string(HTML_TEMPLATE, content=html_content)

@app.route('/append', methods=['POST'])
def append():
    reply = request.form.get('reply')
    if reply:
        with open(HANDOFF_FILE, 'a') as f:
            f.write(f"\n\n## User Reply (Web Interface)\n{reply}\n")
    return redirect(url_for('index'))

if __name__ == '__main__':
    print(f"Starting Handoff Server on http://localhost:5000")
    print(f"Watching file: {HANDOFF_FILE}")
    app.run(port=5000, debug=True)
