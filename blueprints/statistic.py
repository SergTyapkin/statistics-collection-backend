from flask import Blueprint, request

from constants import *
from storage.storage import addStatistic, removeStatistic, getServiceStatistics
from utils.utils import jsonResponse

app = Blueprint('statistic', __name__)


@app.route("", methods=["POST"])
def statisticAdd():
    try:
        req = request.json
        service_token = req['service_token']
        text = req.get('text')
        value = req.get('value')
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)
    if text is None and value is None:
        return jsonResponse("Хотя бы одно поле text или value должно быть не пустым", HTTP_INVALID_DATA)

    statistic = addStatistic(service_token, text, value)
    if not statistic:
        return jsonResponse("Не удалось добавить статистику. Возможно, такого сервиса не существует", HTTP_NOT_FOUND)

    return jsonResponse(statistic.toDict())


@app.route("", methods=["DELETE"])
def statisticDelete():
    try:
        req = request.args
        id = int(req['id'])
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    removeStatistic(id)
    return jsonResponse("Запись статистики удалена")

@app.route("", methods=["GET"])
def statisticsGet():
    try:
        req = request.args
        service_token = req['token']
    except:
        return jsonResponse("Не удалось сериализовать json", HTTP_INVALID_DATA)

    res = getServiceStatistics(service_token)
    return jsonResponse({
        "statistics": list(map(lambda s: s.toDict(), res))
    })
