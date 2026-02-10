# RAG Insight

A Retrieval-Augmented Generation (RAG) system designed to ingest documents, index them into a vector database, and provide accurate, source-grounded answers via an API.

This project is built step-by-step with clarity, modularity, and extensibility in mind, making it suitable for academic projects, demos, and real-world experimentation.

---

## 📌 Project Goals

- Build a complete **end-to-end RAG pipeline**
- Keep architecture **simple but scalable**
- Make every step reproducible and understandable
- Clearly separate **data ingestion**, **retrieval**, and **generation**

---

## 🧠 What is RAG?

Retrieval-Augmented Generation combines:
1. **Retrieval** – finding relevant documents using embeddings
2. **Generation** – using an LLM to answer questions grounded in retrieved data

This avoids hallucinations and keeps responses tied to actual sources.

---

## 🗂️ Project Structure

```text
rag-insight/
├── backend/            # FastAPI backend and RAG logic
│   ├── app/
│   │   ├── main.py     # API entry point
│   │   ├── routes.py  # API routes
│   │   ├── config.py  # Environment & config
│   │   └── rag/       # RAG pipeline (added later)
│   └── requirements.txt
│
├── frontend/           # UI (optional / future)
│
├── data/
│   ├── raw/            # Original documents (PDFs, text, etc.)
│   └── index/          # Vector store files
│
├── diagrams/           # Architecture & flow diagrams
│
├── docs/               # Documentation, notes, decisions
│
└── README.md
