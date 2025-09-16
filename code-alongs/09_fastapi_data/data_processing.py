from constants import DATA_PATH
import pandas as pd
from pprint import pprint
import json

df = pd.read_csv(DATA_PATH / "Sales.csv")


class DataExplorer:
    def __init__(self, limit=100):
        self._df = df.head(limit)
        self._df_full = df

    @property
    def df(self): #egenskap
        return self._df # fält

    def summary(self):
        self._df = self._df_full.describe().T.drop(columns="count")
        return self
    
    def filter(self, country):
        filtered_df = self._df_full.query("Country.str.casefold() == @country.casefold()")
        
        filtered_dict = {
            "total_profit": str(filtered_df["Profit"].sum()),
            "total_revenue": str(filtered_df["Revenue"].sum()),
            "number_of_purch": str(len(filtered_df))
            
        }
        return filtered_dict

    def json_response(self):
        json_data = self.df.to_json(
            orient="records"
        )  # plockar df från property. Blir på rader med records, default är kolumner
        return json.loads(json_data)


dataexplorer = DataExplorer()
# print(dataexplorer.json_response())
