from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from jobs.entities.entities import entities as entity_extractor

router = APIRouter(
    prefix="/entities",
    tags=["entities"],
)

class EntityRequest(BaseModel):
    texts: List[str]

class Entity(BaseModel):
    word: str
    entity: str

class EntityResponse(BaseModel):
    entities: List[Entity]

@router.post("/", response_model=EntityResponse)
async def entities(request: EntityRequest):
    entities = entity_extractor(request.texts)

    return EntityResponse(entities=entities)