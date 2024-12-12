import uuid

import storage.SQL_requests as SQL
from connections import DB
from storage.models import Service, Statistic
from utils.utils import times_to_str, list_times_to_str


def addService(name: str):
    token = str(uuid.uuid4())
    write_token = str(uuid.uuid4())
    try:
        service = DB.execute(SQL.insertService, [name, token, write_token, None])
    except:
        service = None
    if not service:
        return None
    return Service(service['token'], service['write_token'], service['name'], service['js_parser_code'],
                   service['registered'])


def addStatistic(service_write_token: str, text: str, value: float, boolean: bool):
    try:
        statistic = times_to_str(DB.execute(SQL.insertStatistics, [service_write_token, text, value, boolean]))
    except:
        statistic = None
    if not statistic:
        return None
    return Statistic(int(statistic['id']), statistic['service_write_token'], statistic['text'], statistic['value'], statistic['bool'],
                     statistic['datetime'])


def getAllServices():
    try:
        services = DB.execute(SQL.selectAllServices, [], manyResults=True)
    except:
        services = []
    return list(
        map(lambda s: Service(s['token'], s['write_token'], s['name'], s['js_parser_code'], s['registered']), services))


def getService(service_token: str):
    try:
        service = DB.execute(SQL.selectServiceByToken, [service_token])
    except:
        service = None
    if not service:
        return None
    return Service(service['token'], service['write_token'], service['name'], service['js_parser_code'], service['registered'])


def getServiceStatistics(service_token: str):
    try:
        statistics = list_times_to_str(
            DB.execute(SQL.selectStatisticsByServiceWriteToken, [service_token], manyResults=True))
    except:
        statistics = []
    return list(map(lambda s: Statistic(s['id'], s['service_write_token'], s['text'], s['value'], s['bool'], s['datetime']), statistics))


def updateServiceName(service_token: str, new_name: str, js_parser_code: str):
    try:
        service = DB.execute(SQL.updateServiceNameByToken, [new_name, js_parser_code, service_token])
    except:
        service = None
    if not service:
        return None
    return Service(service['token'], service['write_token'], service['name'], service['js_parser_code'], service['registered'])


def removeService(service_token: str):
    DB.execute(SQL.deleteServiceByToken, [service_token])


def removeStatistic(statistic_id: int):
    DB.execute(SQL.deleteStatisticsById, [statistic_id])
