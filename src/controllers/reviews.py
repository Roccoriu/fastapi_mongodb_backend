from src.models.review import Review
from src.models.objectid import ObjectId
from src.db.db_connect import connect_db

from pymongo.results import DeleteResult

db = connect_db('winno')


def get_reviews() -> list:
    reviews = []
    for review in db.reviews.find():
        reviews.append(Review(**review))

    return reviews


def get_review(id: str) -> Review:
    return Review(**db.reviews.find_one({'_id': ObjectId(id)}))


def delete_review(id: str) -> DeleteResult:
    return db.reviews.delete_one({'_id': ObjectId(id)})


def update_review(id: str, updated_review: Review) -> Review:
    db.reviews.replace_one(
        {'_id': ObjectId(id)}, dict(updated_review), upsert=True)

    return Review(**db.reviews.find_one({'_id': ObjectId(id)}))
