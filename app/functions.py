import os
import json
from flask import request
DATABASE = os.getenv('DATABASE_FILENAME')
from .exceptions import EmailAlreadyExistError

def check_file_existence() -> None:
     if not os.path.isfile(DATABASE) or os.path.getsize == 0:
        with open(DATABASE, 'w+') as file:
           json.dump([], file, indent=4)

def read_json() -> json:
    with open(DATABASE, 'r') as file:
        return json.load(file)

def verify_email_existence() -> bool:
    data = request.get_json()
    for user in read_json():
        if user['email'] == data['email'].lower():
            return True
        return False

def write_json(new_user: dict) -> None:
    if verify_email_existence():
        raise EmailAlreadyExistError
        
    else:
        json_list = read_json()
        json_list.append(new_user)

        with open(DATABASE, 'w') as file:
            json.dump(json_list, file, indent=4)