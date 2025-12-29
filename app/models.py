from pydantic import BaseModel, Field
from typing import List


class ChunkRequest(BaseModel):
    text: str = Field(
        ..., description="The full text to be chunked for LLM processing."
    )
    max_tokens: int = Field(
        default=4000, description="Maximum tokens allowed per chunk."
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "This is a long document that needs to be split...",
                    "max_tokens": 2000,
                }
            ]
        }
    }


class ChunkResponse(BaseModel):
    chunks: List[str] = Field(..., description="List of text chunks.")
    total_chunks: int = Field(..., description="Total number of chunks generated.")
    total_tokens: int = Field(
        ..., description="Estimated total tokens based on the encoder."
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "chunks": ["Part 1 of the doc...", "Part 2 of the doc..."],
                    "total_chunks": 2,
                    "total_tokens": 1250,
                }
            ]
        }
    }


class ExtractionResponse(BaseModel):
    full_text: str = Field(..., description="The complete text extracted from the PDF.")
    total_pages: int = Field(..., description="Total pages processed.")
    filename: str = Field(..., description="Name of the processed file.")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "full_text": "Extracted content from the legal document...",
                    "total_pages": 5,
                    "filename": "contract.pdf",
                }
            ]
        }
    }
