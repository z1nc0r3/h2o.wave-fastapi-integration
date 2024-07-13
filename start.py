from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from multiprocessing import Process

# Import Wave app to ensure it's registered
import app
from Train.predictor import Predictor

# Create FastAPI instance
api = FastAPI()

# FastAPI endpoint for prediction
@api.post("/predict")
async def predict(make: str, model: str, condition: str, aml_model: str):
    predictor = Predictor()
    # Assuming Predictor class has a method to predict directly from parameters
    prediction = predictor.predict(make, model, condition, aml_model)
    return JSONResponse(content={"predicted_price": prediction})

def run_wave():
    app.main

def run_fastapi():
    uvicorn.run(api, host="0.0.0.0", port=8000)


def main():
    print('running...')

    # Start both Wave and FastAPI apps
    p1 = Process(target=run_wave)
    p2 = Process(target=run_fastapi)
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
