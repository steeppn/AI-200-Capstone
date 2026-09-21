from fastapi import APIRouter, HTTPException
from models.schemas import messageRequest, messageResponse
from agent import process_message

router = APIRouter()

@router.post("/echo", response_model=messageResponse)
async def echo (request: messageRequest):
    reply = process_message(request.message)
    
    # process_message returns None when there's an exception
    if reply is None:
        raise HTTPException(
            status_code=502,
            detail = "The refund agent did not return a response",
        )
    return messageResponse(message=reply)

    