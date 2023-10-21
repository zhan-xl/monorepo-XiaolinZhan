from ..src.main import *


test_db = {
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


def test_get_root():
    response = get_root()
    assert response == {"Dogs": test_db}

def test_get_dog_by_id():
    response = get_dog_by_id(1)
    assert response == {"dog": test_db[1]}

def test_get_dog_by_name():
    response = get_dog_by_name("charlie")
    assert response == {
        "dog": 
            {
            "ID": 1,
            "Name": "charlie",
            "Breed": "golden retriever",
            "Favorite Food": "penut butter"
            }
    }
    response = get_dog_by_name("lucas")
    assert response ==  {"message": "No dog can be found."}
    

def test_get_dog_by_breed_and_food():
    response = get_dog_by_breed_and_food("golden retriever", "penut butter")
    assert response == {
        "dog": 
            {
            "ID": 1,
            "Name": "charlie",
            "Breed": "golden retriever",
            "Favorite Food": "penut butter"
            }
    }

    response = get_dog_by_breed_and_food("ausie", "watermelon")
    assert response == {"message": "No dog can be found."}