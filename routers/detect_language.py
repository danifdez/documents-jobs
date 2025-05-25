from fastapi import APIRouter
from pydantic import BaseModel
from jobs.detect_language.detect_language import detect_language

router = APIRouter(
    prefix="/language",
    tags=["language"],
)

class LanguageRequest(BaseModel):
    text: str

class LanguageResponse(BaseModel):
    language: str

@router.post("/", response_model=LanguageResponse)
async def language(request: LanguageRequest):
    language = detect_language(request.text)
    return LanguageResponse(language=language)