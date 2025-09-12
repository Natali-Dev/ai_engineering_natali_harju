import pandas as pd
# b) Make an API endpoint where you serve table 3 in JSON format for a read operation.

# def read_data(): 
# df = pd.read_excel("resultat-ansokningsomgang-2024(1).xlsx", sheet_name="Tabell 3", header=5)
# df_cleaned = df.drop(columns=['SUN5 inriktning','Diarienummer','Beviljade platser utbildningsomgång 1','Beviljade platser utbildningsomgång 2','Beviljade platser utbildningsomgång 3','Beviljade platser utbildningsomgång 4','Beviljade platser utbildningsomgång 5','SeQF nivå', 'Sökta platser per utbildningsomgång','Sökta utbildningsomgångar','Beviljade utbildningsomgångar'])
#     json_file = df_cleaned.to_dict(orient="records")
#     return json_file

import json 
from fastapi.responses import JSONResponse

class DataExplorer: 
    def __init__(self, df, limit=100):
        self._df_full = df
        self._df = df.head(limit)
        
    @property
    def df(self): 
        return self._df

    def json_response(self):
        json_data = self._df.to_json(orient="records")
        return JSONResponse(json.loads(json_data))
    
    def filter(self, school, field): 
        df = self._df_full
        if school: 
            df = df[df['Utbildningsanordnare administrativ enhet'].str.contains(school, case=False)] #.query("'Utbildningsanordnare administrativ enhet' == @school")
        if field: 
            df = df[df["Utbildningsområde"].str.contains(field, case=False)]

        sum_status = {
            "Beviljad": len(str(df[df["Beslut"] == "Beviljad"])),
            "Avslag": len(str(df[df["Beslut"] == "Avslag"])),
            
        }
        return  sum_status, df.to_dict(orient="records")
    
    def kpi_status(self): 
        df = self._df_full
        
        # sum_status = len(df[df["Beslut"].str.contains(status, case=False)])
        sum_status = {
            "Beviljad": len(str(df[df["Beslut"] == "Beviljad"])),
            "Avslag": len(str(df[df["Beslut"] == "Avslag"])),
            
        }
        
        return sum_status
        
        
    