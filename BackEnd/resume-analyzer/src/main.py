from fastapi import FastAPI
from src.resume.router import router as resume_router

app = FastAPI(title="Resume Analyzer API")

app.include_router(resume_router)