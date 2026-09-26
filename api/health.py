from fastapi import APIRouter, Request, status, HTTPException

router = APIRouter()

@router.get("/health/liveness")
async def liveness_probe():
        return{"status": "ALIVE"}

@router.get("/health/readiness")
async def readiness_probe(request: Request):
   agent = getattr(request.app.state, "refund_agent", None)

   if agent is None:
       raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="agent or credentials missing, NOT READY",
            )
   
   return{"status": "READY"}
