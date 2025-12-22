# PDF RAG Processor

Optimized PDF extraction and token-aware chunking pipeline for LLM context windows (Pure Python).

## Setup & Installation

1. **Install Dependencies**
   ```bash
   uv sync
   ```

2. **Prepare Your PDF**
   Place a PDF file named `sample.pdf` in the project directory.

## Running the Script

```bash
uv run main.py
```

## Example Output

```
--- RAG Readiness Check ---
Total Tokens: 751
Status: Document is small enough for a single LLM call.

--- FIRST CHUNK READY FOR LLM CONTEXT (500 chars sample)---
INDEPENDENT CONTRACTOR AGREEMENT This Agreement is entered into on this 21st Day of December, 2025, between **ExampleCorp.com** (the "Company") and **Surya Elidanto** (the "Contractor"). 1. Scope of Work The Contractor shall provide services as an **AI Software Engineer** focusing on the development and maintenance of custom automation workflows using Python, FastAPI, and N8N. The primary focus shall be the optimization of client data parsing and security protocols. 2. Compensation and Payment T...
Total Chunks Generated: 1
--------------------------------------------------
```

## How It Works

1. **Extract Text**: Uses `pypdf` to pull clean text from PDF (no AI needed).
2. **Count Tokens**: Uses `tiktoken` to calculate how many tokens the text contains.
3. **Smart Chunking**: If the document exceeds the token limit (default: 4000), it splits the text into smaller chunks that fit within AI context windows.
4. **Output**: Returns an array of text chunks ready to be sent to OpenAI, Gemini, or any LLM.

## Use Cases

- Prepare legal documents for AI summarization
- Extract contract details for automated processing
- Clean up messy PDFs before sending to RAG systems
- Batch process invoices or reports for LLM analysis
