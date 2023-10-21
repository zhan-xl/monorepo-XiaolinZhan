import json
from fastapi import FastAPI, Body

app = FastAPI()

db = {
    1: 
        {
        "ID": 1,
        "Name": "charlie",
        "Breed": "golden retriever",
        "Favorite Food": "penut butter"
        },
    2:            
        {
        "ID": 2,
        "Name": "wally",
        "Breed": "golden retriever",
        "Favorite Food": "cucumber"
        }
}


# get request with no parameter
@app.get("/dog")
def get_root():
    return {"Dogs": db}


# get request with path parameter
@app.get("/dog/{id}")
def get_dog_name(id: int):
    return {"dog": db[id]}


# get request with query parameter
@app.get("/dog/")
def get_dog_by_name(name: str = ""):
    for dog in db.values():
        if dog["Name"] == name.lower():
            return {"dog": dog}
    return {"message": "No dog can be found."}


# get request with path and query parameters
@app.get("/dog/breedandfood/{dog_breed}")
def get_dog_by_breed_and_food(dog_breed: str, food: str = ""):
    dogs = []
    for dog in db.values():
        if dog["Breed"] == dog_breed and dog["Favorite Food"] == food:
            dogs.append(dog)
    return {"dogs": dogs}


# post request
@app.post("/dog")
def create_dog(new_dog=Body()):
    print(new_dog)
    return {"dog": new_dog}


# put request
@app.put("/dog")
def edit_dog(new_dog=Body()):
    return {"dog": new_dog}

# delete request
@app.delete("/dog/{id}")
def delete_dog(id: int):
    if db.has_key(id):
        del db[id]
        return {"message": "Dog has been successfully deleted."}
    else:
        return {"message": "Can not find dog with this ID."}