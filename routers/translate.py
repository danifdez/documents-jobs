from fastapi import APIRouter
from jobs.translate.translate import translate
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/translate",
    tags=["translate"],
)

class TranslateRequest(BaseModel):
    source: str
    target: str
    texts: List[str]

class TranslateResponse(BaseModel):
    translated_texts: List[str]

@router.post("/", response_model=TranslateResponse)
async def translate_texts(request: TranslateRequest) -> TranslateResponse:
    translated_texts = translate(
        source=request.source,
        target=request.target,
        texts=request.texts
    )
    return TranslateResponse(translated_texts=translated_texts)