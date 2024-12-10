from flask import Blueprint, request

from constants import *
from storage.storage import addService, removeService, getService, getAllServices, updateServiceName
from utils.utils import jsonResponse

app = Blueprint('service', __name__)


@app.route("/", methods=["POST"])
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

    return jsonResponse(service.toDict())


@app.route("/", methods=["DELETE"])
def serviceDelete():
    try:
        req = request.args
        token = req['token']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    removeService(token)
    return jsonResponse("Сервис удален")

@app.route("/", methods=["GET"])
def serviceGet():
    try:
        req = request.args
        token = req['token']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    res = getService(token)
    if not res:
        return jsonResponse("Сервис не найден", HTTP_NOT_FOUND)

    return jsonResponse(res.toDict())

@app.route("/all", methods=["GET"])
def serviceGetAll():
    res = getAllServices()
    return jsonResponse({
        "services": list(map(lambda r: r.toDict(), res))
    })

@app.route("/", methods=["PUT"])
def serviceUpdate():
    try:
        req = request.json
        token = req['token']
        new_name = req['new_name']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    res = updateServiceName(token, new_name)
    if not res:
        return jsonResponse("Сервис не найден", HTTP_NOT_FOUND)

    return jsonResponse(res.toDict())
