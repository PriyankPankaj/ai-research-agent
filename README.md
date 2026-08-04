\# AI Research Agent



A multi-agent research assistant that takes a research query, plans a research

strategy, retrieves and reads sources via RAG, and produces a cited report.



\## v1 Scope

\- Planner agent: breaks query into sub-tasks

\- Research agent: web/document retrieval via vector search

\- Reader agent: extracts relevant content from retrieved sources

\- Writer agent: drafts the report

\- Critic agent: reviews draft for gaps/citation accuracy

\- Persistent session memory (SQLite)

\- Dockerized deployment



\## Explicitly out of scope (v1)

\- Multi-user auth

\- Streaming UI (CLI/API only)

\- Fine-tuned models



