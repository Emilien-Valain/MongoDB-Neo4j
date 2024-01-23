from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from fastapi import Query
from typing import Optional

from models import movie, movieUpdate

router = APIRouter()

@router.post("/", response_description="Create a new movie", status_code=status.HTTP_201_CREATED, response_model=movie)
def create_movie(request: Request, movie: movie = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = request.app.database["movies"].insert_one(movie)
    created_movie = request.app.database["movies"].find_one(
        {"_id": new_movie.inserted_id}
    )

    return created_movie

@router.get("/", response_description="List all movies", response_model=List[movie])
def list_movies(request: Request):
    movies = list(request.app.database["movies"].find(limit=100))
    return movies

@router.get("/{title]", response_description="Get a single movie by title or actor")
def find_movie(request: Request,
               movie_name: Optional[str] = Query(None, alias="title"),
               actor_name: Optional[str] = Query(None, alias="actor")):
    query = {}
    if movie_name:
        query["title"] = movie_name
    elif actor_name:
        query["cast"] = actor_name

    if query:
        movie = request.app.database["movies"].find_one(query)
        if movie is not None:
            return movie
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No search parameters provided")


@router.put("/{title}", response_description="Update a movie", response_model=movie)
def update_movie(title: str, request: Request, movie: movieUpdate = Body(...)):
    movie = {k: v for k, v in movie.dict().items() if v is not None}
    if len(movie) >= 1:
        update_result = request.app.database["movies"].update_one(
            {"title": title}, {"$set": movie}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"movie with Title {title} not found")

    if (
        existing_movie := request.app.database["movies"].find_one({"title": title})
    ) is not None:
        return existing_movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"movie with Title {title} not found")

@router.delete("/{id}", response_description="Delete a movie")
def delete_movie(id: str, request: Request, response: Response):
    delete_result = request.app.database["movies"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"movie with ID {id} not found")








