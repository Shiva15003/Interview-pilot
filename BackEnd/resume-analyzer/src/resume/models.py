from pydantic import BaseModel
from typing import List


class ResumeAnalysisResponse(BaseModel):
    overall_score: int
    ats_score: int
    strengths: List[str]
    weaknesses: List[str]
    improvement_suggestions: List[str]
    rephrased_bullets: List[str]
    missing_keywords: List[str]
    final_summary: str