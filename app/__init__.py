from flask import Flask, request
import os

from .functions import DATABASE, check_file_existence, read_json, write_json
from .exceptions import EmailAlreadyExistError, NameOrEmailTypeError

DIRECTORY = os.getenv('FILE_DIRECTORY')

if not os.path.exists(DIRECTORY):
    os.mkdir(DIRECTORY)

app = Flask(__name__)

@app.get('/user')
def check_content():
    check_file_existence()

    return {"data": read_json()}, 200

@app.post("/user")
def send_content():
    check_file_existence()
    json_file = read_json()
    data = request.get_json()
    
    try:
        if type(data["nome"]) != str or type(data["email"]) != str:
            raise NameOrEmailTypeError

        user = {"email": data['email'].lower(), 
            "id": len(json_file) + 1,
            "nome": data['nome'].title(),
        }

        write_json(user)

    except EmailAlreadyExistError:
        return {"error": "Email already exists."}, 409
    
    except NameOrEmailTypeError:
        return {"wrong fields": [
        {
            "nome": type(data["nome"]).__name__
        },
        {
            "email": type(data["email"]).__name__
        }
    ]}, 400

    return {'data': user}, 201