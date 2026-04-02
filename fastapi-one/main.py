from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from ly.views import ly
from ch01.views import router
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(ly)
app.include_router(router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
