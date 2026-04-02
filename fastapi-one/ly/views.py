from fastapi import APIRouter


ly = APIRouter(prefix="/ly", tags=["ly"])

@ly.get("/")
async def root():
    return {"message": "Hello World"}