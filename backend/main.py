from fastapi import FastAPI
from pydantic import BaseModel 
from .hallucination_checker import check_text

app = FastAPI(title="VibeValidator API", version="0.1.0")

class ValidateRequest(BaseModel):
    text: str
    
class ValidateResponse(BaseModel):
    received_text: str
    flagged: list[dict]

@app.get("/")
def read_root():
    return {"status": "ok", "message": "VibeValidator API is running"}  
@app.post("/validate" , response_model=ValidateResponse)
def validate_text(request: ValidateRequest):
    result = check_text(request.text)
    return result
