import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("model.joblib")


class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running"}


@app.post("/predict")
def predict(data: DiabetesInput):
    input_data = pd.DataFrame([data.model_dump()])

    prediction = int(model.predict(input_data)[0])

    label = "Diabetic" if prediction == 1 else "Not diabetic"

    return {
        "prediction": prediction,
        "label": label
    }