from data_processing import read_data
from fastapi import FastAPI

data = read_data()
app = FastAPI()

# schools = data.get("Utbildningsanordnare administrativ enhet")

# b) Make an API endpoint where you serve table 3 in JSON format for a read operation.


@app.get("/data")
async def get_data():
    return data


# c) Make endpoints where you could filter out a particular school.


@app.get("/data/filter_school")
async def filter_school(answer: str):
    schools = []
    for row in data:
        if answer in row.get("Utbildningsanordnare administrativ enhet"):
            schools.append(row)
    return schools


# d) Make endpoints where you could filter out a particular field.


@app.get("/data/filter_field")
async def filter_field(answer: str):
    fields = []
    for row in data:
        if answer in row.get("SUN5 inriktning namn"):
            fields.append(row)
    return fields


# e) Make endpoint for approved (beviljad) and one for not approved (avslag).

@app.get("/data/approved")
async def approved():
    return len([row for row in data if row.get("Beslut") == "Beviljad"])
        
        
@app.get("/data/declined")
async def declined():
    return len([row for row in data if row.get("Beslut") == "Avslag"])
        

# f) Make an endpoint for some KPIs that you think is interesting for a particular stakeholder in mind.

@app.get("/data/kommun")
async def kommun(answer: str):
    # a = approved()
    # d = declined()
    k = len(row for row in data if row.get("Kommun") in answer) 
    my_kpis = {
        "number of applications in {answer}": 10 #k
    }
    return k
    
# g) What else do you want to be able to serve?
