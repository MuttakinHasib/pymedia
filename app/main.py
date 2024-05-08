from fastapi import APIRouter, FastAPI


app = FastAPI()
router = APIRouter()


@app.get("/")
async def root():
    return {"message": "Assalamualaikom, Welcome to the PyMedia!"}


app.include_router(router)
