import nltk.tokenize
import nltk
from fastapi import FastAPI
from routers import dataset, model, corpus, compare, utility
from internal import DB
from fastapi.middleware.cors import CORSMiddleware
from config import Config

nltk.download('punkt')

DB()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
app.include_router(dataset.router)
app.include_router(model.router)
app.include_router(corpus.router)
app.include_router(compare.router)
app.include_router(utility.router)