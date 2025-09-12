import pandas as pd
import pydantic
# b) Make an API endpoint where you serve table 3 in JSON format for a read operation.

def read_data(): 
    df = pd.read_excel("resultat-ansokningsomgang-2024(1).xlsx", sheet_name="Tabell 3", header=5)
    df_cleaned = df.drop(columns=['SUN5 inriktning','Diarienummer','Beviljade platser utbildningsomgång 1','Beviljade platser utbildningsomgång 2','Beviljade platser utbildningsomgång 3','Beviljade platser utbildningsomgång 4','Beviljade platser utbildningsomgång 5','SeQF nivå', 'Sökta platser per utbildningsomgång','Sökta utbildningsomgångar','Beviljade utbildningsomgångar'])
    json_file = df_cleaned.to_dict(orient="records")
    return json_file

