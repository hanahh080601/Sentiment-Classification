from models.comment import Comment
from pymongo import MongoClient
from config.mongodb import Settings

settings = Settings()
conn = MongoClient(settings.DB_CONNECTION_STRING)