import uuid
from datetime import datetime
from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel, Field

class Awards(BaseModel):
    wins: int
    nominations: int
    text: str

class IMDB(BaseModel):
    rating: float
    votes: int
    id: int

class Viewer(BaseModel):
    rating: float
    numReviews: int
    meter: int

class Critic(BaseModel):
    rating: float
    numReviews: int
    meter: int

class Tomatoes(BaseModel):
    viewer: Viewer
    critic: Critic
    lastUpdated: datetime

class movie(BaseModel):
    id: ObjectId = Field(default_factory= str, alias="_id")
    plot: str
    genres: List[str]
    runtime: int
    cast: List[str]
    poster: str
    title: str
    fullplot: str
    languages: List[str]
    released: datetime
    directors: List[str]
    rated: str
    awards: Awards
    lastupdated: datetime
    year: int
    imdb: IMDB
    countries: List[str]
    type: str
    tomatoes: Optional[Tomatoes] = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "title": "Inception",
                "release_year": 2010,
                "genres": ["Action", "Adventure", "Sci-Fi"],
                "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                "runtime": 148,
                "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
                "poster": "http://example.com/poster.jpg",
                "fullplot": "Inception is a sci-fi action thriller that travels around the globe and into the intimate and infinite world of dreams.",
                "languages": ["English", "Japanese", "French"],
                "released": "2010-07-16",
                "directors": ["Christopher Nolan"],
                "rated": "PG-13",
                "awards": {
                    "wins": 86,
                    "nominations": 204,
                    "text": "Won 4 Oscars. Another 82 wins & 204 nominations."
                },
                "lastupdated": "2023-10-12T00:00:00Z",
                "year": 2010,
                "imdb": {
                    "rating": 8.8,
                    "votes": 2000000,
                    "id": 1375666
                },
                "countries": ["USA", "UK"],
                "type": "movie",
                "tomatoes": {
                    "viewer": {
                        "rating": 8.5,
                        "numReviews": 350000,
                        "meter": 91
                    },
                    "critic": {
                        "rating": 7.5,
                        "numReviews": 250,
                        "meter": 85
                    },
                    "lastUpdated": "2023-10-12T00:00:00Z"
                }
            }
        }

class movieUpdate(BaseModel):
    title: Optional[str]
    release_year: Optional[int]
    genre: Optional[List[str]]
    plot: Optional[str]
    genres: Optional[List[str]]
    runtime: Optional[int]
    cast: Optional[List[str]]
    poster: Optional[str]
    fullplot: Optional[str]
    languages: Optional[List[str]]
    released: Optional[datetime]
    directors: Optional[List[str]]
    rated: Optional[str]
    awards: Optional[Awards]
    lastupdated: Optional[datetime]
    year: Optional[int]
    imdb: Optional[IMDB]
    countries: Optional[List[str]]
    type: Optional[str]
    tomatoes: Optional[Tomatoes]

    class Config:
        schema_extra = {
            "example": {
                "title": "Inception",
                "release_year": 2010,
                "genres": ["Action", "Adventure", "Sci-Fi"],
                "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                "runtime": 148,
                "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
                "poster": "http://example.com/poster.jpg",
                "fullplot": "Inception is a sci-fi action thriller that travels around the globe and into the intimate and infinite world of dreams.",
                "languages": ["English", "Japanese", "French"],
                "released": "2010-07-16",
                "directors": ["Christopher Nolan"],
                "rated": "PG-13",
                "awards": {
                    "wins": 86,
                    "nominations": 204,
                    "text": "Won 4 Oscars. Another 82 wins & 204 nominations."
                },
                "lastupdated": "2023-10-12T00:00:00Z",
                "year": 2010,
                "imdb": {
                    "rating": 8.8,
                    "votes": 2000000,
                    "id": 1375666
                },
                "countries": ["USA", "UK"],
                "type": "movie",
                "tomatoes": {
                    "viewer": {
                        "rating": 8.5,
                        "numReviews": 350000,
                        "meter": 91
                    },
                    "critic": {
                        "rating": 7.5,
                        "numReviews": 250,
                        "meter": 85
                    },
                    "lastUpdated": "2023-10-12T00:00:00Z"
                }
            }
        }