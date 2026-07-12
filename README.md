# AI Chatbot Assistant

A simple, interactive **command-line chatbot** powered by a Large Language Model
(LLM). It talks to the **Groq API** using an OpenAI-compatible client, keeps track
of your conversation history, and runs entirely in your terminal.

This guide walks you through everything you need to run the chatbot on a fresh
machine — no prior knowledge of the project required.

![alt text](/assets/images/image.png)
---

## What You Get

- 💬 Interactive chat loop in your terminal
- 🧠 Conversation memory (the bot remembers earlier messages in the session)
- ⚙️ Configurable model, temperature, and token limits via environment variables
- 🔌 Powered by [Groq](https://groq.com/) through an OpenAI-compatible API
- ✅ A small test suite you can run to confirm everything works

---

## Prerequisites

Install these before you start:

| Requirement | Notes |
|-------------|-------|
| **Python 3.13+** | Required. Check with `python --version`. |
| **[uv](https://docs.astral.sh/uv/)** | Fast Python package & environment manager (install steps below). |
| **A Groq API key** | Free — create one at <https://console.groq.com/keys>. |
| **Git** | Optional, only if you want to clone the repo. |
| **Visual Studio Code** | Optional, any editor/terminal works. |

---

## Quick Start (TL;DR)

If you already have `uv` and a Groq API key, run these from the project folder:

```powershell
uv sync                       # install dependencies
copy .env.example .env        # create your env file (Windows)
# then edit .env and set GROQ_API_KEY=your_key_here
uv run main.py                # start chatting
```

For a step-by-step walkthrough, keep reading.

---

## Step 1: Get the Project

If you have the project folder already, open it in VS Code and skip to Step 2.

Otherwise, clone or download it, then open the folder:

```bash
git clone <repository-url>
cd AI-Chatbot-Assistant
```

---

## Step 2: Install `uv`

`uv` manages the virtual environment and dependencies for you.

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen your terminal, then verify:

```bash
uv --version
```

---

## Step 3: Install Dependencies

From the project root, run:

```bash
uv sync
```

This automatically:

1. Creates a virtual environment in a `.venv` folder.
2. Installs everything declared in `pyproject.toml` (and pinned in `uv.lock`).

> You do **not** need to manually create or activate the virtual environment when
> you use `uv run`. `uv` handles it for you. (If you prefer to activate it anyway,
> see [Optional: Activate the Virtual Environment](#optional-activate-the-virtual-environment).)

---

## Step 4: Configure Your API Key

The chatbot needs a Groq API key to work.

1. Copy the example environment file:

   ```powershell
   copy .env.example .env      # Windows
   ```

   ```bash
   cp .env.example .env        # macOS/Linux
   ```

2. Open `.env` and paste your key:

   ```text
   GROQ_API_KEY=your_key_here
   ```

> 🔐 The `.env` file holds a secret and is git-ignored. **Never commit it.**

### Optional Settings

You can override these defaults in `.env` (all optional):

| Variable      | Default          | Description                             |
|---------------|------------------|-----------------------------------------|
| `PROVIDER`    | `groq`           | LLM provider name.                      |
| `MODEL`       | `qwen/qwen3-32b` | Model identifier to use.                |
| `TEMPERATURE` | `0.3`            | Sampling randomness, `0.0`–`2.0`.       |
| `MAX_TOKENS`  | `500`            | Maximum tokens in a single reply, `> 0`.|

Invalid values (e.g. a non-numeric `TEMPERATURE`) cause the app to fail
immediately at startup with a clear error message.

---

## Step 5: Run the Chatbot

```bash
uv run main.py
```

You should see a welcome banner. Type a message, press **Enter**, and the AI
replies.

### Chat Commands

| Command  | Description                    |
|----------|--------------------------------|
| `/help`  | Show the list of commands      |
| `/clear` | Clear the conversation history |
| `/exit`  | Exit the chatbot               |

You can also press **Ctrl+C** to quit at any time.

---

## Run the Tests

Confirm everything is wired up correctly:

```bash
uv run pytest
```

The tests live in the `tests/` folder and do not require a network connection or
API key.

---

## Project Structure

```text
AI-Chatbot-Assistant/
│
├── main.py                     # Entry point: the interactive chat loop
├── config.py                   # Loads and validates configuration/env vars
├── pyproject.toml              # Project metadata and dependencies
├── .env.example                # Template for your local .env file
├── README.md                   # This guide
│
├── src/
│   ├── conversation/
│   │   └── conversation_manager.py   # Tracks message history
│   ├── models/
│   │   └── message.py                # Message data model
│   ├── prompts/
│   │   └── system_prompt.py          # Defines the assistant's persona
│   ├── providers/
│   │   └── groq_provider.py          # Talks to the Groq API
│   ├── services/
│   │   └── llm_service.py            # Routes requests to the provider
│   └── utils/
│       └── logger.py                 # Logging helper
│
└── tests/                      # Test suite
    ├── test_conversation.py
    └── test_message.py
```

---

## Troubleshooting

| Problem | Cause & Fix |
|---------|-------------|
| `GROQ_API_KEY is not set` | You skipped Step 4. Create `.env` and set `GROQ_API_KEY`. |
| `uv: command not found` | `uv` isn't installed or your terminal wasn't restarted. Redo Step 2 and open a new terminal. |
| `TEMPERATURE must be a number...` (or similar) | An invalid value is set in `.env`. Fix it to match the ranges in [Optional Settings](#optional-settings). |
| `Something went wrong while contacting the AI` | Network issue, invalid API key, or Groq outage. Check your internet connection and confirm your key at <https://console.groq.com/keys>. |
| Python version errors | This project needs **Python 3.13+**. Check with `python --version` and upgrade if needed. |

---

## Optional: Activate the Virtual Environment

`uv run` doesn't require manual activation, but if you want an activated shell
(for running `python`, `pytest`, etc. directly):

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

When active, your prompt shows `(.venv)`.

---

## Useful `uv` Commands

| Command | Description |
|---------|-------------|
| `uv sync` | Install/update dependencies from `pyproject.toml` |
| `uv add <package>` | Add a new dependency |
| `uv run main.py` | Run the chatbot |
| `uv run pytest` | Run the test suite |
| `uv pip list` | List installed packages |
| `uv venv` | Create a virtual environment manually |

