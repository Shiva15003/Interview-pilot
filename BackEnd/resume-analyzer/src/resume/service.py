from .file_parser import (
    extract_text_from_pdf,
    extract_text_from_docx,
    clean_text
)
from .prompt_builder import build_resume_prompt
from ..core.llm_engine import call_llm


def analyze_resume(file_bytes: bytes, extension: str) -> dict:

    if extension == "pdf":
        extracted_text = extract_text_from_pdf(file_bytes)
    elif extension == "docx":
        extracted_text = extract_text_from_docx(file_bytes)
    else:
        raise Exception("Unsupported file format")

    cleaned_text = clean_text(extracted_text)

    if not cleaned_text:
        raise Exception("Unable to extract resume content")

    prompt = build_resume_prompt(cleaned_text)

    result = call_llm(prompt)

    return result