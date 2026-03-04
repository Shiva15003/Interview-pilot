from fastapi import APIRouter, UploadFile, File, HTTPException
from ..core.config import MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS
from .service import analyze_resume
from .models import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(status_code=400, detail="File is required")

    extension = file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file format")

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    try:
        result = analyze_resume(contents, extension)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))