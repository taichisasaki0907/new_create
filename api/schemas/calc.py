from pydantic import BaseModel


class CalcPowRequest(BaseModel):
    input: int