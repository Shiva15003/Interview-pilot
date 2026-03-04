def build_resume_prompt(resume_text: str) -> str:
    return f"""
You are an expert ATS resume evaluator and technical hiring manager with experience in pointing out mistakes and suggesting the right pointers missing in the resume.

Analyze the resume below.

Return ONLY valid JSON in this EXACT structure:

{{
  "overall_score": number (0-100),
  "ats_score": number (0-100),
  "strengths": [string],
  "weaknesses": [string],
  "improvement_suggestions": [string],
  "rephrased_bullets": [string],
  "missing_keywords": [string],
  "final_summary": string
}}

STRICT RULES:
- Return ONLY JSON.
- Do not add explanations.
- Do not wrap in markdown.
- Do not add comments.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""