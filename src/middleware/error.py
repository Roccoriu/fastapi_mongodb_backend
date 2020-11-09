from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from pymongo import errors


class DuplicateKeyError(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        response = await call_next(request)

        return response
