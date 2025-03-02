from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="Library API",
    description="API for managing books and authors",
    version="1.0.0"
)

# Ruta para crear un autor
@app.post("/authors", tags=["Authors"])
async def create_author(data: dict):
    name = data["name"]
    bio = data["bio"]

    return {
        "status_code": 200,
        "message": f"Author {name} created successfully with the ID {str(uuid.uuid4())}",
    }

# Ruta para crear un libro
@app.post("/books", tags=["Books"])
async def create_book(title: str, author_id: str, price: float):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": f"Book '{title}' by author ID {author_id} created with price {price}",
                "id": str(uuid.uuid4())
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# Ruta para obtener información de un autor
@app.get("/authors/{author_id}", tags=["Authors"])
async def get_author(author_id: str):
    authors_db = {
        "1": {
            "name": "Gabriel Garcia Marquez",
            "bio": "Colombian novelist, short-story writer, screenwriter, and journalist."
        },
        "2": {
            "name": "Isabel Allende",
            "bio": "Chilean writer known for novels such as 'The House of the Spirits'."
        }
    }

    try:
        author = authors_db[author_id]
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Author {author['name']}, Bio: {author['bio']}"
            }
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )