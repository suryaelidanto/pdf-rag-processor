from fastapi import FastAPI, UploadFile, File, HTTPException
from app.models import ChunkRequest, ChunkResponse, ExtractionResponse
from app.services import extract_text_from_pdf_bytes, get_llm_ready_chunks

app = FastAPI(
    title="PDF RAG Processor API",
    description="Microservice for extracting text from PDFs and generating LLM-optimized chunks.",
    version="1.0.0",
)


@app.get("/")
async def health_check():
    return {"status": "ok", "service": "PDF RAG Processor"}


@app.post("/extract", response_model=ExtractionResponse)
async def extract_pdf(file: UploadFile = File(...)):
    """Extract full text from an uploaded PDF file."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        content = await file.read()
        text, pages = extract_text_from_pdf_bytes(content)
        return ExtractionResponse(
            full_text=text, total_pages=pages, filename=file.filename
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF Processing Error: {str(e)}")


@app.post("/chunk", response_model=ChunkResponse)
async def chunk_text(data: ChunkRequest):
    """Split provided text into chunks based on token limits."""
    try:
        chunks, total_tokens = get_llm_ready_chunks(data.text, data.max_tokens)
        return ChunkResponse(
            chunks=chunks, total_chunks=len(chunks), total_tokens=total_tokens
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chunking Error: {str(e)}")
