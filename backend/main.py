from fastapi import FastAPI
from pydantic import BaseModel 
app = FastAPI(title="VibeValidator API", version="0.1.0")

class ValidateRequest(BaseModel):
    text: str
    
class ValidateResponse(BaseModel):
    received_text: str
    flagged: list[str]

@app.get("/")
def read_root():
    return {"status": "ok", "message": "VibeValidator API is running"}  
@app.post("/validate" , response_model=ValidateResponse)
def validate_text(request: ValidateRequest):
    return {
        "received_text": request.text,
        "flagged": []
        }
