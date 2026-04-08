from fastapi import APIRouter

from api.schemas.calc import CalcPowRequest

router = APIRouter()


@router.post("/calc_pow")
async def calc_pow(req: CalcPowRequest):
    square = req.input ** 2
    return {"ans": square}