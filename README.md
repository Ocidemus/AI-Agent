# 🧠 Agentic Code Editor with Google Gemini

A toy code editor agent, inspired by Claude Code and Cursor’s agent mode. This project walks through how to build an **LLM-powered code assistant** using the **free Google Gemini API**, Python function calling, and feedback loops.

> 🔧 The final result is a local tool that can analyze Python files, detect bugs, and modify code — all through intelligent agentic reasoning.

---

## 📚 Chapter Overview

### 1. **LLMs**
Learn how LLMs process prompts, and how to interact with the Gemini API via the official Python client.

### 2. **Functions**
Write real functions for file operations, such as:
- Reading and writing files
- Listing project contents
- Running Python scripts

### 3. **Function Calling**
Enable Gemini to call your tools directly using structured function-calling (via `types.FunctionDeclaration` and `Part.function_call`).

### 4. **Agents**
Introduce a feedback loop: let the model reason step-by-step, inspect tool results, and iteratively improve code.

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.8+
- A free [Google AI Studio](https://aistudio.google.com/app/apikey) API key
- `google-generativeai` client

### 🔧 Installation

```bash
git clone https://github.com/yourusername/agentic-code-editor.git
cd agentic-code-editor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set your API key:

```bash
export GOOGLE_API_KEY="your-key-here"
```
▶️ Usage
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

🧪 Features
✅ Agentic loop with up to 20 iterations

✅ Gemini 1.5 / 2.0 support

✅ Structured function-calling with validation

✅ Real-time feedback from executed code

📂 Project Structure
```bash
.
├── main.py                  # Entry point
├── tools/                   # File system functions (read, write, list, run)
├── agent/                   # Agent loop + Gemini interaction
├── config.py                # API config and system prompt
├── calculator/              # Sample project to inspect/fix
└── README.md
```
🛠️ Built With
Google Gemini API

Python 3

Function calling (types.FunctionDeclaration, Part.function_call)

Feedback loop design pattern

📄 License
MIT License © 2025 Your Name

