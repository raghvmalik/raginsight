from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1")


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    return {
        "answer": f"Processed your question: {request.question}",
        "sources": ["doc_alpha.pdf", "page_12"]
    }


@router.post("/ingest")
async def ingest_documents():
    return {"message": "Document ingestion endpoint (not implemented yet)"}


@router.get("/health")
async def health_check():
    return {"status": "healthy", "project": "RAGInsight"}