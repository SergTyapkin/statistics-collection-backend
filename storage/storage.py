import uuid

import storage.SQL_requests as SQL
from connections import DB
from storage.models import Service, Statistic
from utils.utils import times_to_str, list_times_to_str


def addService(name: str):
    token = uuid.uuid4()
    service = DB.execute(SQL.insertService, [name, token])
    if not service:
        return None
    return Service(service['token'], service['name'])

def addStatistic(service_token: str, text: str, value: float):
    statistic = times_to_str(DB.execute(SQL.insertStatistics, [service_token, text, value]))
    if not statistic:
        return None
    return Statistic(statistic['service_token'], statistic['text'], statistic['value'], statistic['datetime'])

def getAllServices():
    services = DB.execute(SQL.selectAllServices, [], manyResults=True)
    return list(map(lambda s: Service(s['token'], s['name']), services))


def getService(service_token: str):
    service = DB.execute(SQL.selectServiceByToken, [service_token])
    if not service:
        return None
    return Service(service['token'], service['name'])


def getServiceStatistics(service_token: str):
    statistics = list_times_to_str(DB.execute(SQL.selectStatisticsByServiceToken, [service_token], manyResults=True))
    return list(map(lambda s: Statistic(s['service_token'], s['text'], s['value'], s['datetime']), statistics))


def updateServiceName(service_token: str, new_name: str):
    service = DB.execute(SQL.updateServiceNameByToken, [new_name, service_token])
    if not service:
        return None
    return Service(service['token'], service['name'])


def removeService(service_token: str):
    DB.execute(SQL.deleteServiceByToken, [service_token])


def removeStatistic(statistic_id: int):
    DB.execute(SQL.deleteStatisticsById, [statistic_id])
