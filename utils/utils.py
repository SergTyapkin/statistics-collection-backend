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

        config["db_host"] = os.environ.get("DATABASE_HOST") or config["db_host"]
        config["db_port"] = os.environ.get("DATABASE_PORT") or config["db_port"]
        config["db_user"] = os.environ.get("DATABASE_USER") or config["db_user"]
        config["db_db"] = os.environ.get("DATABASE_DB") or config["db_db"]
        config["db_password"] = os.environ.get("DATABASE_PASSWORD") or config["db_password"]

        config["api_host"] = os.environ.get("API_HOST") or config["api_host"]
        config["api_port"] = os.environ.get("API_PORT") or config["api_port"]

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


def time_prettify(time: datetime.datetime):
    return time.strftime("%d.%m.%Y %H:%M:%S")
