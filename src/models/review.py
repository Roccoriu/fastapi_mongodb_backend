from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

from .objectid import PyObjectId


class Review(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    project: str
    slug: str
    description: str
    projectPage: str
    rating: int
    imagePath: str
    projectOwnerEmail: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
