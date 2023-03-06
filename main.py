from fastapi import FastAPI
from pydantic import BaseModel
from app.routers import book, user, file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# uvicorn app.main:app --reload

# CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost:8080",
    "http://localhost:3000",
    "https://stackpython.co"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add routers
app.include_router(book.router)
app.include_router(user.router)
app.include_router(file.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

'''
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
'''
