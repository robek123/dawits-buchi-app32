from fastapi import APIRouter, Depends
from ..core.config import settings

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": settings.PROJECT_NAME}
