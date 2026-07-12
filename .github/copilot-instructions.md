# Copilot Instructions — AI Chatbot Assistant

## Project overview
A command-line chatbot powered by an LLM. It talks to the **Groq API** through the
OpenAI-compatible client, tracks conversation history in memory, and runs entirely
in the terminal. This is a small, learning-focused Python project — keep it simple.

## Tech stack
- **Python 3.13+** (uses modern typing: `list[dict[str, str]]`, `Literal`, `dataclass`)
- **uv** for environment and dependency management (`pyproject.toml` + `uv.lock`)
- **openai** client (pointed at Groq's base URL)
- **python-dotenv** for loading `.env`
- **pytest** for tests

## Common commands
```bash
uv sync            # install dependencies
uv run main.py     # start the chatbot
uv run pytest      # run the test suite (no network/API key needed)
```
Always run Python via `uv run` — do not assume a manually activated venv.

## Architecture & layering
Requests flow one direction through clear layers. Respect these boundaries:

```
main.py                        # interactive chat loop, command handling (/help, /clear, /exit)
  └─ ConversationManager       # src/conversation/ — holds message history
  └─ ask_llm (llm_service)     # src/services/ — routes to the configured provider
       └─ ask_groq             # src/providers/ — the only place that calls the Groq API
config.py                      # loads + validates env vars, fails fast on bad values
src/models/message.py          # Message dataclass (role + content)
src/prompts/system_prompt.py   # assistant persona / system prompt
src/utils/logger.py            # logging helper
```

Rules:
- `main.py` never calls a provider directly — it goes through `ask_llm`.
- Provider-specific code (API URLs, client setup) lives **only** in `src/providers/`.
- To add a provider, add a `src/providers/<name>_provider.py` and route to it in
  `ask_llm` based on the `PROVIDER` config value.
- Messages passed to the LLM are `list[dict[str, str]]` with `role`/`content` keys.
  Use `Message.to_dict()` to produce that shape.

## Configuration
- All config comes from `config.py`, sourced from env vars (`.env` for local dev).
- Vars: `PROVIDER`, `MODEL`, `TEMPERATURE` (0.0–2.0), `MAX_TOKENS` (>0), plus the
  secret `GROQ_API_KEY`.
- Config is validated at import time and raises `ValueError` on bad input — keep this
  fail-fast behavior. Do not silently fall back to defaults for invalid values.
- **Never** hardcode secrets or commit `.env`. Read `GROQ_API_KEY` from the environment.

## Coding conventions
- Add module-level and function docstrings (triple-quoted), matching the existing style.
- Use full type hints on function signatures.
- Prefer small, single-purpose functions and pure data models (`@dataclass(frozen=True)`).
- Document raised exceptions in a `Raises:` section of the docstring.
- Keep user-facing terminal output plain and simple (this is a CLI app).
- Surface provider/network errors gracefully in the chat loop rather than crashing.

## Testing
- Tests live in `tests/` and must run **without** a network connection or API key.
- Do not add tests that make real Groq API calls — mock the provider/client instead.
- Run with `uv run pytest` before considering a change complete.

## Things to avoid
- Don't bypass the service/provider layering.
- Don't add heavy frameworks or dependencies — keep the project lightweight.
- Don't over-engineer; only implement what's requested.
