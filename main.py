import numpy as np
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="CDLRecognizeAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    raise HTTPException(status_code=200)

