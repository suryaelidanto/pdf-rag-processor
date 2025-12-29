import pypdf
import tiktoken
from typing import List, Tuple
from io import BytesIO

GPT_ENCODING_MODEL: str = "cl100k_base"


def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> Tuple[str, int]:
    """Extract all text and page count from PDF bytes."""
    reader = pypdf.PdfReader(BytesIO(pdf_bytes))
    full_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            clean_text = " ".join(text.split())
            full_text.append(clean_text)

    return "\n\n".join(full_text).strip(), len(reader.pages)


def get_llm_ready_chunks(text: str, max_tokens: int) -> Tuple[List[str], int]:
    """
    Splits text into chunks based on token count for LLM context optimization.
    Returns: (List of chunks, total_tokens)
    """
    encoder = tiktoken.get_encoding(GPT_ENCODING_MODEL)
    tokens = encoder.encode(text)
    total_tokens = len(tokens)

    if total_tokens <= max_tokens:
        return [text], total_tokens

    token_ratio = total_tokens / len(text)
    chunk_char_size = int(max_tokens / token_ratio)

    chunks = [
        text[i : i + chunk_char_size] for i in range(0, len(text), chunk_char_size)
    ]

    return chunks, total_tokens
