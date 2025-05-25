from fastapi import FastAPI
from routers import translate, extraction, entities
from routers import detect_language

app = FastAPI()

app.include_router(translate.router)
app.include_router(extraction.router)
app.include_router(entities.router)
app.include_router(detect_language.router)