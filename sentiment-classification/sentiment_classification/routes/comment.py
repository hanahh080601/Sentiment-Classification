from fastapi import APIRouter
from database.database import conn
from schemas.comment import commentEntity, commentEntities

comment = APIRouter()

@comment.get('/')
async def list_all_comments():
    return commentEntities(conn.hanlhn.comments.find())
