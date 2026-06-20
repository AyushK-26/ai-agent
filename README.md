# AI Research Agent

A small Python-based AI agent built using LangChain and OpenAI.

This project takes a research query from the user, searches the web for relevant information, generates a structured summary, and can optionally save the research output to a text file if requested.

## What It Does

The agent performs the following steps:

1. Accepts a research topic from the user
2. Uses a web search tool to gather information
3. Generates a structured response containing:
   - Topic
   - Summary
   - Sources

4. Saves the research output into a text file when explicitly asked

---

## Tech Used

- Python
- LangChain
- OpenAI API (`gpt-4o-mini`)
- DuckDuckGo Search
- UV (package management)

---

## Project Structure

```text
ai-agent/
│
├── research/          # Generated research files
├── main.py            # Main application entry point
├── tools.py           # Agent tool definitions
├── pyproject.toml     # Dependencies and project config
├── uv.lock            # Locked dependency versions
└── README.md
```

---

## How to Run

Install dependencies:

```bash
uv sync
```

Set environment variable in `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the program:

```bash
python main.py
```

---

## Example Query

```text
Research skateboarding culture
```

Example with saving:

```text
Research skateboarding culture and save it to a file
```

---

## Example Output

```json
{
  "topic": "Skateboarding Culture",
  "summary": "Skateboarding culture is centered around creativity, self-expression, and community...",
  "sources": ["DuckDuckGo Search"]
}
```

Saved files are stored inside the `research/` folder.

---

## Purpose

This project was created for learning and experimentation with:

- AI agents
- Tool calling
- Prompt design
- Structured output generation
- LangChain workflows
