# 📹 Agentic AI YouTube Analyzer

An AI-powered application built with **Agno** (formerly Phidata) that analyzes YouTube videos using multi-agent workflows. The system can process video contents, generate summaries, answer queries, and maintain interaction memory.

---

## 🌟 Features

* **YouTube Video Analysis:** Extract insights, transcriptions, and summaries directly from YouTube video URLs.
* **Agentic Workflows:** Multi-agent setup (`teams.py`, `agent.py`) utilizing Agno agents to break down complex user queries.
* **Interactive UI:** Web interface (`ui.py`) for analyzing videos based on streamlit.
* **Memory & Storage:** Persistent session and conversation memory using a local database backend (`agno.db`).

---

## 🛠️ Project Structure

```text
AgenticAI_Agno/
├── agent.py               # Core agent initialization and configuration
├── teams.py               # Multi-agent coordination logic
├── memory.py              # Conversation memory & session handling
├── ui.py                  # User Interface application (Streamlit / Gradio)
├── youtube_analyzer.py    # YouTube integration & processing logic
├── .env.example           # Example file for environment variables
├── .gitignore             # Excluded files (venv, .env, agno.db)
└── README.md              # Project documentation