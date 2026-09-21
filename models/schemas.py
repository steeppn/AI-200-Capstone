from pydantic import BaseModel


class messageRequest(BaseModel):
    """ Request model for echo endpoint. """
    message: str

class messageResponse(BaseModel):
    """ Response model for echo endpoint. """
    message: str


