from data_processing import DataExplorer
from fastapi import FastAPI, Query, APIRouter
from contextlib import asynccontextmanager
import pandas as pd
from pathlib import Path
import json
from fastapi.responses import JSONResponse

DATA_PATH = Path(__file__).parent 

@asynccontextmanager # Cost efficent, läs in df en gång
async def lifespan(app: FastAPI): 
    app.state.df = pd.read_excel(DATA_PATH / "resultat-ansokningsomgang-2024(1).xlsx", sheet_name="Tabell 3", header=5).drop(columns=['SUN5 inriktning','Diarienummer','Beviljade platser utbildningsomgång 1','Beviljade platser utbildningsomgång 2','Beviljade platser utbildningsomgång 3','Beviljade platser utbildningsomgång 4','Beviljade platser utbildningsomgång 5','SeQF nivå', 'Sökta platser per utbildningsomgång','Sökta utbildningsomgångar','Beviljade utbildningsomgångar'])
    yield
    del app.state.df
    
app = FastAPI(lifespan=lifespan)
#     
# data = read_data()
# app = FastAPI()

# b) Make an API endpoint where you serve table 3 in JSON format for a read operation.


@app.get("/data")
async def get_data():
    data = DataExplorer(app.state.df)
    return data.json_response()


# # c) Make endpoints where you could filter out a particular school.
# # d) Make endpoints where you could filter out a particular field.


@app.get("/data/filter")
async def read_filter(school: str = Query(None), field: str = Query(None)):
    data = DataExplorer(app.state.df)
    return data.filter(school, field)

# # e) Make endpoint for approved (beviljad) and one for not approved (avslag).


@app.get("/data/total_approved")
async def approved():
    data = DataExplorer(app.state.df)
    return data.kpi_status()


# # f) Make an endpoint for some KPIs that you think is interesting for a particular stakeholder in mind.


# @app.get("/data/kommun")
# async def kommun(answer: str):
#     # a = approved()
#     # d = declined()
#     k = len(row for row in data if row.get("Kommun") in answer)
#     my_kpis = {"number of applications in {answer}": 10}  # k
#     return k


# g) What else do you want to be able to serve?
