# PDF RAG Processor

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-ready microservice designed to handle the heavy lifting of PDF text extraction and token-aware chunking for RAG (Retrieval-Augmented Generation) workflows.

## Features
- **FastAPI Core**: High-performance asynchronous endpoints.
- **Precision Extraction**: Clean text extraction from PDFs using `pypdf`.
- **Token-Aware Chunking**: Uses `tiktoken` to ensure chunks fit perfectly within LLM context windows.
- **Production Infrastructure**: Standardized `Makefile`, `Dockerfile`, and CI/CD.

---

## Prerequisites
- **Python**: 3.10+
- **UV**: Fast Python package manager
- **Make**: Build automation tool
- **Docker**: For containerized deployment

---

## Usage

### 1. Setup & Installation
```bash
make setup
```

### 2. Run Development Server
```bash
make dev
```
The API will be available at `http://localhost:8000`. Access `/docs` for Swagger UI.

### 3. API Scenarios

#### Scenario: Extract Text from PDF
**Request:** `POST /extract` (Multipart File)
**Output:**
```json
{
  "full_text": "Extracted document content...",
  "total_pages": 5,
  "filename": "sample.pdf"
}
```

#### Scenario: Generate LLM-Ready Chunks
**Request:** `POST /chunk`
```json
{
  "text": "Long document text...",
  "max_tokens": 1000
}
```
**Output:**
```json
{
  "chunks": ["Part 1...", "Part 2..."],
  "total_chunks": 2,
  "total_tokens": 1850
}
```

---

## Roadmap
- [x] Initial FastAPI modularization.
- [x] Token-aware chunking logic.
- [ ] Support for OCR (Optical Character Recognition) for scanned PDFs.
- [ ] Multi-format support (DOCX, HTML).

---

## Development
- **Linting**: `make lint`
- **Testing**: `make test`
- **Container**: `make up`
