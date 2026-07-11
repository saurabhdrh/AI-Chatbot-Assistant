# Project Setup Guide

This guide explains how to set up the project using **VS Code** and **uv**, a fast Python package and virtual environment manager.

## Prerequisites

Before you begin, ensure you have:

- Visual Studio Code
- Python 3.10 or later
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

Install all required packages from the `requirements.txt` file:

```bash
uv add -r requirements.txt
```

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

---

## Project Structure (Example)

```text
project-name/
│
├── src/
├── main.py
├── requirements.txt
├── pyproject.toml
├── uv.lock
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
| `uv add -r requirements.txt` | Install packages from requirements file |
| `uv pip list` | List installed packages |
| `uv run main.py` | Run the application |
| `uv sync` | Synchronize dependencies from `pyproject.toml` |