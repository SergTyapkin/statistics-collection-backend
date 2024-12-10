import datetime
import json
import os
from flask import jsonify, make_response

from constants import HTTP_OK


def read_config(filepath: str) -> dict:
    try:
        file = open(filepath, "r", encoding='utf-8')
        config = json.load(file)
        file.close()

        if "db_host" not in config:
            config["db_host"] = os.environ["DATABASE_HOST"]
        if "db_port" not in config:
            config["db_port"] = os.environ["DATABASE_PORT"]
        if "db_user" not in config:
            config["db_user"] = os.environ["DATABASE_USER"]
        if "db_db" not in config:
            config["db_db"] = os.environ["DATABASE_DB"]
        if "db_password" not in config:
            config["db_password"] = os.environ["DATABASE_PASSWORD"]

        if "api_host" not in config:
            config["api_host"] = os.environ["API_HOST"]
        if "api_port" not in config:
            config["api_port"] = os.environ["API_PORT"]

        return config
    except Exception as e:
        print("Can't open and serialize json:", filepath)
        print(e)
        exit()


def times_to_str(object):
    for key in object.keys():
        if type(object[key]) is datetime.time:
            object[key] = object[key].isoformat()
        if type(object[key]) is datetime.date:
            object[key] = object[key].isoformat()
    return object


def list_times_to_str(listWithTimedelta):
    for el in listWithTimedelta:
        times_to_str(el)
    return listWithTimedelta


def jsonResponse(resp: dict or str, code: int = HTTP_OK):
    if isinstance(resp, str):
        resp = {"info": resp}

    return make_response(jsonify(resp), code)
