from pydantic import BaseModel, Field, ValidationError
from fastapi import FastAPI
import json

with open("fastapi_glossary.json", "r") as file:
    text = file.read()
    text_json = json.loads(text)


class Glossary(BaseModel):
    id: int
    word: str
    meaning: str


valid_glossary = []
for t in text_json:
    try:
        valid_glossary.append(Glossary.model_validate(t))
    except ValidationError as err:
        print(err)

# words = [w.word for w in valid_glossary]
# meaning = [m.meaning for m in valid_glossary]
# word_dict = {
#     "words": [w.word for w in valid_glossary],
#     "meaning": [m.meaning for m in valid_glossary]
# }
# a) Now create an endpoint `/glossary` which will return all words and their meaning.

app = FastAPI()


# READ
@app.get("/glossary")
async def read_glossary():
    # for text in valid_glossary:
    #     return text.word, text.meaning  # _json)
    return valid_glossary


# b) Create a query parameter to filter out a specific word


@app.get("/glossary/find_word")
async def find_word(word: str):
    return [v for v in valid_glossary if v.word.casefold() == word.casefold()]


# c) Turn your API into a CRUD API, so that you can add glossary, update and delete glossary.

# CREATE


@app.post("/glossary/create_word")
async def create_word(word: Glossary):
    new_word = Glossary.model_validate(word)
    valid_glossary.append(new_word)
    return new_word


# UPDATE


@app.put("/glossary/update_word")
async def update_word(updated_word: Glossary):
    for i, glos in enumerate(valid_glossary):
        if glos.id == updated_word.id:
            valid_glossary[i] = updated_word
        return updated_word


# DELETE

@app.delete("/glossary/delete_word/{id}")
async def delete_word(id: int):
    for i, glos in enumerate(valid_glossary):
        if id == glos.id:
            del valid_glossary[i]


# d) Test out your API in Swagger UI.

# e) Test out your API using requests inside of a Jupyter notebook or a separate Python script. Try the different request types.
