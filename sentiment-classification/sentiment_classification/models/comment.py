from pydantic import BaseModel

class Comment(BaseModel):
    comment: str 
    sentiment: str