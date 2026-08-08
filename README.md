\# AutoLab AI — Autonomous AI Research \& Engineering Platform



AutoLab AI is a multi-agent system that acts as an AI Research Engineer: given

a high-level objective, it plans the work, gathers information, verifies

findings, and produces structured reports — combining Agentic AI (planning,

multi-agent collaboration, memory, reflection) with Generative AI (LLMs, RAG,

report generation).



\## Architecture



!\[AutoLab AI architecture](docs/architecture.svg)



\## What's built (v1)



\- \*\*5-agent pipeline\*\* — Planner, Researcher, Reader, Writer, Critic, each with

&#x20; a shared interface (`BaseAgent`) and a common state object (`ResearchState`)

&#x20; passed through the pipeline

\- \*\*RAG pipeline\*\* — Chroma vector store with sentence-transformer embeddings,

&#x20; wired into the Research Agent for semantic document retrieval

\- \*\*Multi-tool framework\*\* — Wikipedia lookup, calculator, and web search

&#x20; tools behind a shared `BaseTool` interface, with keyword-based tool

&#x20; selection and graceful fallback on external API failures

\- \*\*Long-term memory\*\* — a separate Chroma-backed `MemoryManager` that recalls

&#x20; relevant findings from \*previous\* research sessions when a new, related

&#x20; query comes in (proven working across differently-worded queries)

\- \*\*Session persistence\*\* — SQLite-backed session store; a research run can

&#x20; be started via the API, and its progress/result queried later even after

&#x20; the process restarts

\- \*\*FastAPI backend\*\* — `POST /research` to start a session,

&#x20; `GET /research/{id}` to check status/result, with the pipeline running as

&#x20; a background task

\- \*\*Citation-based reports\*\* — the Writer agent produces a structured report

&#x20; with numbered citations mapped to a Sources section; the Critic agent

&#x20; performs a real (if simple) quality check — flagging thin source counts or

&#x20; short drafts rather than always approving

\- \*\*Dockerized\*\* — full `Dockerfile` + `docker-compose.yml`, builds and runs

&#x20; the complete stack in a container, verified working end-to-end

\- \*\*Tests\*\* — pytest suite covering the orchestrator pipeline and tool

&#x20; selection/execution



\## Known limitations (honest, not hidden)



\- Tool selection is keyword-based, not LLM-driven — the `describe()` method

&#x20; on each tool is already shaped for a future swap to real function-calling

\- Vector store weak-match filtering isn't implemented yet — a query with no

&#x20; good matches still returns its best (bad) matches rather than saying "no

&#x20; relevant sources found"

\- The Wikipedia tool occasionally hits transient API failures (handled

&#x20; gracefully, but not retried with backoff yet)

\- Planner's subtask decomposition is currently a stand-in (single subtask,

&#x20; no real breakdown) pending LLM integration



\## Roadmap (post-placement — full AutoLab AI vision)



\- Coding Agent — generates and executes code iteratively

\- Benchmark Agent — automates model evaluation (latency, memory, accuracy)

\- Verification Agent — cross-checks facts across multiple sources

\- LLM-driven planning and tool selection (replacing current heuristics)

\- Relevance-score thresholding for retrieval

\- Knowledge graph integration (NetworkX)

\- LangGraph-based orchestration (replacing the current custom orchestrator)

\- Artifact types beyond reports: PPT generation, benchmark visualizations

\- Streamlit UI

\- Qwen 3/4 (quantized) as the core LLM, deployable on Colab T4



\## Tech stack (v1)



Python · FastAPI · SQLite · ChromaDB · sentence-transformers · Docker · pytest



\## Tech stack (full vision)



Python · LangGraph · Qwen 3/4 (Quantized) · FAISS · BGE-M3 · SQLite + FAISS ·

PyMuPDF · NetworkX · Streamlit



\## Running locally



```bash

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt

python -m uvicorn src.api.main:app --reload

```



\## Running with Docker



```bash

docker compose up --build

```



\## Running tests



```bash

python -m pytest tests\\ -v

```

