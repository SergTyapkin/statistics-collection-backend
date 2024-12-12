from flask import Blueprint, request

from constants import *
from storage.storage import addService, removeService, getService, getAllServices, updateServiceName
from utils.utils import jsonResponse

app = Blueprint('service', __name__)


@app.route("", methods=["POST"])
def serviceCreate():
    try:
        req = request.json
        name = req['name']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)
    name = name.strip()

    service = addService(name)
    if not service:
        return jsonResponse("Не удалось создать сервис. Имя уже занято", HTTP_DATA_CONFLICT)

    return jsonResponse(service.toDict(True))


@app.route("", methods=["DELETE"])
def serviceDelete():
    try:
        req = request.args
        token = req['token']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    removeService(token)
    return jsonResponse("Сервис удален")


@app.route("", methods=["GET"])
def serviceGet():
    try:
        req = request.args
        token = req['token']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    res = getService(token)
    if not res:
        return jsonResponse("Сервис не найден", HTTP_NOT_FOUND)

    return jsonResponse(res.toDict(True))


@app.route("/all", methods=["GET"])
def serviceGetAll():
    res = getAllServices()
    return jsonResponse({
        "services": list(map(lambda r: r.toDict(False), res))
    })


@app.route("", methods=["PUT"])
def serviceUpdate():
    try:
        req = request.json
        token = req['token']
        new_name = req.get('new_name')
        js_parser_code = req.get('js_parser_code')
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    service = getService(token)
    if not service:
        return jsonResponse("Сервис не найден", HTTP_NOT_FOUND)

    new_name = new_name or service.name
    js_parser_code = js_parser_code or service.js_parser_code

    res = updateServiceName(token, new_name, js_parser_code)
    if not res:
        return jsonResponse("Сервис не найден", HTTP_NOT_FOUND)

    return jsonResponse(res.toDict(True))
