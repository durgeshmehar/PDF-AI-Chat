from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from utils.file_handler import handle_file_upload
from utils.query_handler import handle_query

from api import users, chat, pdf
from db.db_setup import engine
from db.models import user
from core.settings import settings, PROJECT_DIR
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse

origins = [ "*" ]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user.Base.metadata.create_all(bind=engine)


 
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(chat.router, prefix="/chats", tags=["chats"])
app.include_router(pdf.router, prefix="/pdf", tags=["pdf"])

