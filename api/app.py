from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))
app = FastAPI()

# Define schema
class InputData(BaseModel):
    data: list

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.post("/predict")
def predict(input: InputData):
    data = np.array(input.data).reshape(1, -1)
    prediction = model.predict(data)[0]

    return {
        "prediction": int(prediction),
        "result": "Fraud" if prediction == 1 else "Normal"
    }