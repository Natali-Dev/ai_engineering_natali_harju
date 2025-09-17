import joblib
from pathlib import Path
from fastapi import FastAPI, APIRouter
import pandas as pd
from pydantic import BaseModel
import array
DATA_PATH = Path(__file__).parent

app = FastAPI()
router = APIRouter(prefix="/mpg")

model = joblib.load(DATA_PATH / "models/mpg.joblib")

df = (
    pd.read_csv(DATA_PATH / "auto-mpg.csv")
    .drop(columns=["mpg", "car name", "origin"])
    .rename(columns={"model year": "model_year"})
)
df = df[df["horsepower"] != "?"]


class Miles(BaseModel):
    cylinders: float
    displacement: float
    horsepower: float
    weight: float
    acceleration: float
    model_year: float


class ModelPrediction(BaseModel):
    predicted_miles: float


miles = []
miles_dict = df.to_dict(orient="records")
for data in miles_dict:
    miles.append(Miles.model_validate(data))
# e) Read this model and create an API around it. You should have endpoints to be able to read the data, do some filterings and be able to send in data to get prediction back.


# Read data
@router.get("")
async def read_data():
    return miles


# Filter data


@router.get("/filter")
async def filter_data(cylinder: float):
    filtered_data = []
    for data in miles:
        if data.cylinders == cylinder:
            filtered_data.append(data)
    return filtered_data


# Predict data


@router.post("/predict", response_model=ModelPrediction)
async def predict_miles(user_input: Miles):
    data_to_predict = pd.DataFrame([user_input.model_dump()])

    y_pred = model.predict(data_to_predict)
    return {
        "predicted_miles": float(y_pred[0])}

    


# print(df.head())

app.include_router(router=router)
