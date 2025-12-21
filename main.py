import pypdf
import tiktoken
import os
from typing import Optional, List

MAX_TOKENS: int = 4000
INPUT_PDF_PATH: str = "sample.pdf"
GPT_ENCODING_MODEL: str = "cl100k_base"


def extract_text_from_pdf(pdf_path: str) -> Optional[str]:
    """Extract all text from a given PDF file path."""
    try:
        with open(pdf_path, "rb") as file:
            reader = pypdf.PdfReader(file)
            full_text = []

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    clean_text = " ".join(text.split())
                    full_text.append(clean_text)

            return "\n\n".join(full_text).strip()

    except FileNotFoundError:
        print(f"ERROR: File not found at {pdf_path}")
        return None
    except Exception as e:
        print(f"AN ERROR OCCURED: {e}")
        return None


def get_llm_ready_chunks(text: str) -> List[str]:
    """
    Checks token count and cuts the text into chunks ready for RAG/LLM context window.
    """

    try:
        encoder = tiktoken.get_encoding(GPT_ENCODING_MODEL)
        tokens = encoder.encode(text)
        total_tokens = len(tokens)

        print("\n--- RAG Readiness Check ---")
        print(f"Total Tokens: {total_tokens}")

        if total_tokens <= MAX_TOKENS:
            print("Status: Document is small enough for a single LLM call.")
            return [text]

        print(f"ALERT: Document requires chunking (Max Token: {MAX_TOKENS}).")

        token_ratio = total_tokens / len(text)
        chunk_char_size = int(MAX_TOKENS / token_ratio)

        chunks = [
            text[i : i + chunk_char_size] for i in range(0, len(text), chunk_char_size)
        ]

        print(f"Result: Split into {len(chunks)} chunks.")
        return chunks

    except Exception as e:
        print(f"AN ERROR OCCURED during token processing: {e}")
        return [text]


def main():
    if not os.path.exists(INPUT_PDF_PATH):
        print("-" * 50)
        print(
            f"SETUP REQUIRED: Please place a PDF document named '{INPUT_PDF_PATH}' in this directory."
        )
        print("-" * 50)
    else:
        clean_doc_text = extract_text_from_pdf(INPUT_PDF_PATH)

        if clean_doc_text:
            llm_chunks = get_llm_ready_chunks(clean_doc_text)

            print("\n--- FIRST CHUNK READY FOR LLM CONTEXT (500 chars sample)---")
            print(llm_chunks[0][:500] + "...")
            print(f"Total Chunks Generated: {len(llm_chunks)}")
            print("-" * 50)


if __name__ == "__main__":
    main()
