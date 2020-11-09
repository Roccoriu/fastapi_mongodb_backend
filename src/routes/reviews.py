from fastapi import APIRouter
from pymongo import errors
from starlette.responses import Response
from src.models.review import Review
from src.db.db_connect import connect_db
from bson import ObjectId

from src.controllers import reviews as review_controller

router = APIRouter()
db = connect_db('winno')


@router.get('/reviews')
async def list_reviews():
    reviews = review_controller.get_reviews()

    return {'count': len(reviews), 'result': reviews}


@router.get('/reviews/{id}')
async def get_review(id):
    review = review_controller.get_review(id)

    return {'count': 1, 'result': [review]}


@router.delete('/reviews/{id}')
async def delete_review(id, response: Response):
    result = review_controller.delete_review(id)

    if result.deleted_count == 0:
        response.status_code = 404
        return {'status': 'failed', 'result': 'Document not found'}

    return {'status': 'ok', 'result': id}


@router.put('/reviews/{id}')
async def update_review(id, updated_review: Review, response: Response):
    try:
        response.status_code = 202
        result = db.reviews.replace_one(
            {'_id': ObjectId(id)}, dict(updated_review), upsert=True)

        return {'status': 'ok', 'result': id}

    except:
        response.status_code = 404
        return {'status': 'failed', 'result': 'Document not found'}


@router.post('/reviews')
async def post_review(new_review: Review, response: Response):
    try:
        response.status_code = 201
        result = db.reviews.insert_one(dict(new_review))
        return {'status': 'ok', 'result': str(result.inserted_id)}

    except errors.DuplicateKeyError:
        result = None
        response.status_code = 409

    return {'status': 'failed', 'result': 'Identical Doument exists'}
