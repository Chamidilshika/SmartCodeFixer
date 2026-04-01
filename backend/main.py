from fastapi import FastAPI
from pydantic import BaseModel
from model import summarize_code, detect_bug, fix_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.get("/")
def home():
    return {"message": "AI Code Assistant is running "}

@app.post("/summarize")
def summarize(input: CodeInput):
    summary = summarize_code(input.code)
    return {"summary": summary}

@app.post("/detect-bug")
def detect(input: CodeInput):
    result = detect_bug(input.code)
    return {"issues": result}

@app.post("/fix-code")
def fix(input: CodeInput):
    result = fix_code(input.code)
    return {"fixed_code": result}