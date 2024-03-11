from typing import Annotated
from fastapi import APIRouter, Depends
from app.app import oauth2_scheme


router = APIRouter(tags=["docs"])


@router.get("/")
async def root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Hello World " + token}
