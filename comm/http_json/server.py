from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoRequest(BaseModel):
    text: str

class EchoResponse(BaseModel):
    text: str

@app.post("/echo", response_model=EchoResponse)
def echo(req: EchoRequest) -> EchoResponse:
    # "Complementary DTO": append " world!"
    return EchoResponse(text=req.text + " world!")