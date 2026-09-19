from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_message

app = FastAPI(
    title = 'refund_app',
    description = 'handles the refund process through AI',
    version = '0.1.0',
)

class RefundRequest(BaseModel):
    message: str

@app.get('/')
async def root():
    return {'message': 'API is running'}

@app.post('/echo')
async def echo(request: RefundRequest):
    response = process_message(request.message)
    return {'reply': response}

