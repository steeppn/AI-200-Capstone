from fastapi import APIRouter, HTTPException, Response, Request, status
from models.schemas import messageRequest, messageResponse

router = APIRouter()

@router.post("/run", response_model=messageResponse)
async def echo (message_request: messageRequest, response: Response, request: Request):
    
    settings = getattr(request.app.state,  "_settings", None)
    agent = getattr(request.app.state, "refund_agent", None)

    if agent is None or settings is None:
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Endpoint or settings not configured"
        )
    if not settings.LLM_MODEL_NAME:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="LLM model name is not set"
        )

    try:
        completions = await agent.process_message(message_request.message)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to process request"
        )
    if completions is None:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The refund agent did not return a response"
        )
    return messageResponse(message=completions)

        