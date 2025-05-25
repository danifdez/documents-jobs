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
    metadata: Optional[dict] = None
    

@router.post("/", response_model=ExtractionResponse)
async def extract_text(request: ExtractionRequest) -> ExtractionResponse:
    extracted_text = extract(request.file)
    return ExtractionResponse(content=extracted_text['content'], title=extracted_text.get('title'), metadata=extracted_text.get('metadata'))
