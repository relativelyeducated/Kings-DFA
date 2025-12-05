import express from 'express';
import cors from 'cors';
import { spawn } from 'child_process';

const app = express();
app.use(cors());
app.use(express.json());

// Generic CLI bridge function
const callCLI = (command, args, fullPrompt) => {
  return new Promise((resolve, reject) => {
    const proc = spawn(command, args, {
      shell: true,
      env: { ...process.env }
    });

    let output = '';
    let errorOutput = '';

    proc.stdout.on('data', (data) => {
      output += data.toString();
    });

    proc.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });

    proc.on('close', (code) => {
      if (code === 0 && output) {
        resolve(output.trim());
      } else {
        reject(new Error(errorOutput || 'Command failed'));
      }
    });

    proc.on('error', (err) => {
      reject(err);
    });
  });
};

// Claude bridge endpoint - uses Anthropic API directly
app.post('/api/claude-code', async (req, res) => {
  const { history, prompt, systemInstruction } = req.body;

  // Get API key from environment
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return res.status(400).json({ error: 'ANTHROPIC_API_KEY not set in environment' });
  }

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1024,
        system: systemInstruction || "You are a strategic planner.",
        messages: [
          { role: 'user', content: `Here is the current plan history:\n${history}\n\nTask: ${prompt}\n\nRespond concisely.` }
        ]
      })
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(`Claude API Error: ${err}`);
    }

    const data = await response.json();
    res.json({ response: data.content[0].text });
  } catch (error) {
    console.error('Claude API error:', error);
    res.status(500).json({ error: error.message });
  }
});

// Gemini bridge endpoint - uses Google API directly
app.post('/api/gemini', async (req, res) => {
  const { history, prompt, systemInstruction, apiKey } = req.body;

  if (!apiKey) {
    return res.status(400).json({ error: 'Gemini API key required' });
  }

  try {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

    const payload = {
      contents: [
        { role: "user", parts: [{ text: `Here is the current plan history:\n${history}\n\nTask: ${prompt}` }] }
      ],
      systemInstruction: { parts: [{ text: systemInstruction || "You are a strategic planner." }] }
    };

    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(`Gemini API Error: ${err}`);
    }

    const data = await response.json();
    res.json({ response: data.candidates[0].content.parts[0].text });
  } catch (error) {
    console.error('Gemini API error:', error);
    res.status(500).json({ error: error.message });
  }
});

// Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', service: 'trimind-claude-bridge' });
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`TriMind Claude Bridge running on http://localhost:${PORT}`);
  console.log('Claude Code integration ready!');
});
