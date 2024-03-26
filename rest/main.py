from fastapi import Depends, FastAPI

from .routers import images

app = FastAPI()


app.include_router(images.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}