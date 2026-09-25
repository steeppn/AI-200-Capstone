from fastapi import APIRouter, Response, Request, status
import logging

router = APIRouter()

is_healthy = True #placeholder
logger = logging.getLogger("ai_agent")

@router.get("/health/liveness")
async def livness_prove(response: Response):

    if is_healthy:
        return{"status": "ALIVE"}

    logger.error("Liveness probe failed!")
    # Can do action here if it fails

    response.status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return{"status": "unhealthy", "reason": "simulated_deadlock"}

@router.get("/health/readiness")
async def readiness_probe(response: Response, request: Request):

   agent = getattr(request.app.state, "refund_agent", None)

   if not agent:
       response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
       return{"status": "NOT READY", "reason": "agent or credentials missing"}

   if not is_healthy:
       response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
       return{"status": "NOT READY", "reason": "system_sabotaged"}