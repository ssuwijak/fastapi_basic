from fastapi import FastAPI
from pydantic import BaseModel # New import
from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

# start web server by (at cli)
# uvicorn main:app --reload

# New
book_db = [
    {
        "title":"The C Programming",
        "price": 720
    },
    {
        "title":"Learn Python the Hard Way",
        "price": 870
    },
    {
        "title":"JavaScript: The Definitive Guide",
        "price": 1369
    },
    {
        "title":"Python for Data Analysis",
        "price": 1394
    },
    {
        "title":"Clean Code",
        "price": 1500
    },
]

# Model
class Book(BaseModel):
    title: str
    price: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/book/")
async def get_books():
    return book_db

@app.get("/book/{book_id}")
async def get_book(book_id: int):
    return book_db[book_id-1]

#create a new book
@app.post("/book")
async def create_book(book: Book):
    book_db.append(book.dict())
    return book_db[-1]

#update the book data
@app.put("/book/{book_id}")
async def edit_book(book_id: int, book: Book):
    result = book.dict()
    book_db[book_id-1].update(result)
    return result

#delete the book
@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
    book = book_db.pop(book_id-1)
    return book

# upload a file
@app.post("/img")
async def up_img_book(file: UploadFile = File(...)):
    size = await file.read()
    return  { "File Name": file.filename, "size": len(size)}


@app.post("/multi-img")
async def up_multi_file(files: List[UploadFile] = File(...)):
    file = [
        {
            "File Name":file.filename, 
            "Size":len(await file.read())
        } for file in files]
    return  file