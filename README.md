# Project Setup Guide

This guide explains how to set up the project using **VS Code** and **uv**, a fast Python package and virtual environment manager.

## Prerequisites

Before you begin, ensure you have:

- Visual Studio Code
- Python 3.13 or later
- Git (optional but recommended)

---

## Step 1: Create/Open the Project in VS Code

- Open **Visual Studio Code**.
- Create a new project folder or open an existing project.

---

## Step 2: Install `uv`

Open a PowerShell terminal in VS Code and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:

```bash
uv --version
```

---

## Step 3: Initialize the Project

Initialize a new Python project:

```bash
uv init
```

This creates the project configuration file (`pyproject.toml`).

---

## Step 4: Create a Virtual Environment

Create a virtual environment using `uv`:

```bash
uv venv
```

This creates a `.venv` folder in your project.

---

## Step 5: Activate the Virtual Environment

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

### macOS/Linux

```bash
source .venv/bin/activate
```

After activation, your terminal prompt should display:

```text
(.venv)
```

---

## Step 6: Install Project Dependencies

Install all dependencies declared in `pyproject.toml` (and pinned in `uv.lock`):

```bash
uv sync
```

---

## Step 7: Configure Environment Variables

This app calls the Groq API and requires an API key.

1. Copy the example file and fill in your key:

   ```bash
   copy .env.example .env   # Windows
   # cp .env.example .env    # macOS/Linux
   ```

2. Edit `.env` and set your key:

   ```text
   GROQ_API_KEY=your_key_here
   ```

The `.env` file is git-ignored and must never be committed. Optional overrides
(`PROVIDER`, `MODEL`, `TEMPERATURE`, `MAX_TOKENS`) are documented in `.env.example`.

---

## Verify the Installation

Check the installed packages:

```bash
uv pip list
```

---

## Run the Application

Start the application using:

```bash
uv run main.py
```

### Chat Commands

Once running, type a message and press Enter to chat. The following commands are
available:

| Command  | Description              |
|----------|--------------------------|
| `/help`  | Show the command list    |
| `/clear` | Clear conversation history |
| `/exit`  | Exit the chatbot         |

### Run the Tests

```bash
uv run pytest
```

---

## Project Structure (Example)

```text
project-name/
│
├── src/
├── main.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── README.md
└── .venv/
```

---

## Useful `uv` Commands

| Command | Description |
|---------|-------------|
| `uv init` | Initialize a new project |
| `uv venv` | Create a virtual environment |
| `uv add <package>` | Install a package |
| `uv sync` | Synchronize dependencies from `pyproject.toml` |
| `uv pip list` | List installed packages |
| `uv run main.py` | Run the application |
| `uv run pytest` | Run the test suite |

