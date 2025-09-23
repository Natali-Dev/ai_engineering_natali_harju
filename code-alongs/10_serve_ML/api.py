from fastapi import FastAPI
from data_processing import IrisInput, PredictionOutput, IrisData
from pydantic import BaseModel, Field
import pandas as pd
import joblib
from constants import MODEL_PATH
app = FastAPI()
iris = IrisData()

@app.get("/api") 
def read_data():
    return iris.to_json()


@app.post("/api/predict", response_model=PredictionOutput) #post för att vi ska skicka in en blomma. Vi tvingar XX att följa klassen (str)
def predict_iris(payload: IrisInput): #payload = det som använderan har fyllt i, och valideras utifrån datatyperna av IrisInput
    data_to_predict = pd.DataFrame([payload.model_dump()]) #model_dump för payload är en pydantic-modell, blir en python-dict, konverteras till en DF eftersom det är det joblob-modellen har tränat på 
    clf = joblib.load(MODEL_PATH / "iris_classifier.joblib")
    prediction = clf.predict(data_to_predict)
    
    return {"predicted_flower": prediction[0]}
    