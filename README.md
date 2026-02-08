# aiAgent26:

# AI Code Debugging Agent

An experimental, agentic code-debugging assistant built as part of the Boot.dev “Build a Code-Fixing Agent” project. The agent uses the Gemini API and function calling to inspect code, run tests, and suggest or apply fixes.

> This is a **toy** agent for learning purposes. Do **not** run it on sensitive codebases or in production environments.

---

## Features

- Uses an LLM (Gemini) to:
  - Analyze error messages and test failures
  - Propose code changes and refactors
  - Explain bugs and reasoning in natural language
- Tool-calling / function-calling to:
  - Read files from the repository
  - Write modified files
  - Run tests or commands in a subprocess
- Simple command-line interface to drive the agent loop

---

## How It Works

At a high level:

1. The user describes a bug or runs into failing tests.
2. The agent:
   - Reads relevant files
   - Optionally runs tests/commands
   - Calls the LLM with the current context
3. The LLM responds with:
   - A plan
   - Proposed edits (via tools)
   - Explanations for what changed and why
4. The loop can repeat until tests pass or the user stops.

The core components are:

- `main.py` (or your entrypoint): starts the agent loop / CLI.
- `agent.py` (or equivalent): orchestrates prompts, tools, and state.
- functions:
  - `call_function(function_call, verbose=False)`
  - `get_file_content(working_directory, file_path)`
  - `get_files_info(working_directory, directory=".")`
  - `write_file(working_directory, file_path, content)`
  - `run_python_file(working_directory, file_path, args=None)`
- ***

## Requirements

- Python 3.10+ (adjust if different)
- `pip` / `venv`
- A Gemini API key

Setup
Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Set up your Gemini API key
Create a .env file (or use your environment of choice) and add:

```bash
GEMINI_API_KEY=your_api_key_here
```

Usage
Adjust these commands to match how you actually invoke the agent.

```bash
uv run main.py
```

Example flows:
Let the agent try to fix failing tests:
Start the agent
Describe the problem or tell it to “run tests and fix failures”
Ask it to refactor or add features:
“Refactor foo.py to reduce duplication in the parsing logic.”
“Add logging to the request handler.”
