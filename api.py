# api.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import h2o
from Train.predictor import Predictor

router = APIRouter()

predictor = Predictor()

class PredictionRequest(BaseModel):
    make: str
    model: str
    condition: str
    aml_model: str

@router.post("/predict")
async def predict(request: PredictionRequest):
    try:
        predicted_price = await predictor.predict_price(
            request.make, request.model, request.condition, request.aml_model
        )
        return {"predicted_price": predicted_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health():
    return {"status": "ok"}