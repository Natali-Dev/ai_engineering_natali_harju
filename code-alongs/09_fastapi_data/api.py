from fastapi import FastAPI, APIRouter
from data_processing import DataExplorer


app = FastAPI()
router = APIRouter(prefix="/api/sales")
# dataexplorer = DataExplorer()


@router.get("")
async def read_sales():
    # implement this code to return json data in this endpoint
    return DataExplorer().json_response()


@router.get("/summary")
async def read_summary_details():
    """shows summary stats"""
    
    return DataExplorer().summary().json_response()

@router.get("/kpis")
async def read_kpis(country: str):
    """KPIs based on country"""
    return DataExplorer().filter(country=country)

# @app.get("/api/sales/filter")

app.include_router(router)
#     return