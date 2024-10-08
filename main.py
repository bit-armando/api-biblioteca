from fastapi import FastAPI
from routes.libros import router as libro_router

app = FastAPI()
app.include_router(libro_router)