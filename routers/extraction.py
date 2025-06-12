from typing import Optional
from fastapi import APIRouter
from jobs.extraction.extractor import extract
from pydantic import BaseModel

router = APIRouter(
    prefix="/extraction",
    tags=["extraction"],
)

class ExtractionRequest(BaseModel):
    file: str

class ExtractionResponse(BaseModel):
    content: str
    title: Optional[str] = None
    author: Optional[str] = None
    publication_date: Optional[str] = None

@router.post("/", response_model=ExtractionResponse)
async def extract_text(request: ExtractionRequest) -> ExtractionResponse:
    extracted_text = extract(request.file)
    return ExtractionResponse(content=extracted_text['content'], title=extracted_text.get('title'), author=extracted_text.get('author'), publication_date=extracted_text.get('publication_date'))
