\# AutoLab AI — Autonomous AI Research \& Engineering Platform



AutoLab AI is a multi-agent system that acts as an AI Research Engineer: given

a high-level objective, it plans the work, gathers information, verifies

findings, and produces structured reports — combining Agentic AI (planning,

multi-agent collaboration, memory, reflection) with Generative AI (LLMs, RAG,

report generation).



\## v1 Scope (placement portfolio build)

\- Planner Agent — decomposes objective into subtasks

\- Research Agent — retrieval via RAG (vector search)

\- Reader Agent — extracts relevant content from sources

\- Artifact Generator (Writer Agent) — drafts cited reports

\- Reflection Agent (Critic) — reviews draft for gaps/accuracy

\- In-memory session state (SQLite persistence added if time allows)

\- FastAPI backend, Dockerized



\## Roadmap (post-placement — full AutoLab AI vision)

\- Coding Agent — generates and executes code iteratively

\- Benchmark Agent — automates model evaluation (latency, memory, accuracy)

\- Verification Agent — cross-checks facts across multiple sources

\- Memory Manager — persistent semantic memory via SQLite + FAISS

\- Knowledge graph integration (NetworkX)

\- LangGraph-based orchestration (replacing the current custom orchestrator)

\- Artifact types beyond reports: PPT generation, benchmark visualizations

\- Streamlit UI

\- Qwen 3/4 (quantized) as the core LLM, deployable on Colab T4



\## Tech Stack (v1)

Python · FastAPI · SQLite · Vector DB (Chroma/FAISS) · Docker



\## Tech Stack (full vision)

Python · LangGraph · Qwen 3/4 (Quantized) · FAISS · BGE-M3 · SQLite + FAISS ·

PyMuPDF · NetworkX · Streamlit

