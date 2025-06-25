# Agentic Code Editor with Google Gemini

A toy code editor agent, inspired by Claude Code and Cursor’s agent mode. This project walks through how to build an **LLM-powered code assistant** using the **free Google Gemini API**, Python function calling, and feedback loops.

> 🔧 The final result is a local tool that can analyze Python files, detect bugs, and modify code — all through intelligent agentic reasoning.

---

A toy code editor agent, inspired by Claude Code and Cursor’s agent mode. This project demonstrates how to build an **LLM-powered code assistant** using the **free Google Gemini API**, Python function calling, and feedback loops.

The agent can:
- Analyze code
- Detect bugs
- Modify files
- Run Python code
All through natural language prompts and Gemini’s tool-calling capabilities.

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.8+
- A free [Google AI Studio](https://aistudio.google.com/app/apikey) API key
- `google-generativeai` client

### 🔧 Installation

```bash
git clone https://github.com/yourusername/AI-Agent.git
cd AI-Agent.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set your API key:

```bash
export GOOGLE_API_KEY="your-key-here"
```
### ▶️ Usage
Ask questions about the codebase like:

```bash
python main.py "how does the calculator render results to the console?"
```
Expected output:

```sql
 - Calling function: get_files_info
 - Calling function: get_file_content
Final response:
<agent explains logic here...>
```
### 🧪 Example Project Included
This repo includes an example project in the calculator/ folder that the agent can analyze and debug.

You can try it out immediately with:

```bash
python main.py "how does the calculator render results to the console?"
```
This will trigger the agent to:

Explore files in the calculator/ project
Read and interpret code logic
Use tool calls to retrieve and analyze the relevant functions


### 🧪 Features
✅ Agentic loop with up to 20 iterations

✅ Gemini 1.5 / 2.0 support

✅ Structured function-calling with validation

✅ Real-time feedback from executed code

📂 Project Structure
```bash
.
├── main.py                  # Entry point for the agent
├── tools/                   # Functions: read/write files, run code, list dirs
├── agent/                   # Core agent logic and feedback loop
├── config.py                # System prompts and setup
├── calculator/              # 🔹 Example Python project for testing the agent
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   ├── render.py
│   │   └── morelorem.txt
│   ├── tests.py
│   └── README.md
└── README.md
```
## 🛠️ Built With

- [Google Gemini API](https://ai.google.dev/)
- Python 3
- Function calling (`types.FunctionDeclaration`, `Part.function_call`)
- Feedback loop design pattern

📄 License
MIT License © 2025 ocidmeus

