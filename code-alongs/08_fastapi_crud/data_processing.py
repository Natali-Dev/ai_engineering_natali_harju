from constants import DATA_PATH
import json 
from pprint import pprint

def read_json(filename: str):
    with open(DATA_PATH / filename, "r") as file: 
        # data = file.read() # är en str! 
        data = json.load(file) # är en dict! 
    return data


if __name__ == "__main__": 
    data = read_json("library.json")
pprint(data)