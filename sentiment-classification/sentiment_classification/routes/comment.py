from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from database.database import conn, add_comment
from schemas.comment import commentEntity, commentEntities
from predict import prediction
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

comment = APIRouter()
comment.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@comment.get('/', response_class=HTMLResponse)
async def list_all_comments(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "list_comments": commentEntities(conn.hanlhn.comments.find())})
    #return commentEntities(conn.hanlhn.comments.find())

@comment.post('/', response_class=HTMLResponse)
async def predict_sentiment(request: Request, comment: str = Form()):
    try:
        pred = prediction.predict(comment)
        await add_comment(comment, pred)
    except Exception as e:
        print(e)
    #return pred
    return templates.TemplateResponse("index.html", {"request": request, "list_comments": commentEntities(conn.hanlhn.comments.find())})