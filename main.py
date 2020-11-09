import uvicorn
from fastapi import FastAPI
from src.routes import reviews
from src.middleware.error import DuplicateKeyError
from src.settings.settings import load_env
from os import getenv

load_env()
app = FastAPI()

app.add_middleware(DuplicateKeyError)


app.include_router(reviews.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=getenv('HOST'),
                port=int(getenv('PORT')), reload=bool(getenv('RELOAD')))
