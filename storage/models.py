from utils.utils import read_config

config = read_config('config.json')


class Service:
    token: int
    name: str

    def __init__(self, token, name):
        self.token = token
        self.name = name

    def __repr__(self):
        return '[SERVICE #' + str(self.name) + ']'

    def toDict(self):
        return {
            'token': self.token,
            'name': self.name,
        }


class Statistic:
    id: int
    service_token: str
    text: str
    value: float
    datetime: str

    def __init__(self, service_token: str, text: str, value: float, datetime: str):
        self.service_token = service_token
        self.text = text
        self.value = value
        self.datetime = datetime

    def __repr__(self):
        return '[STATISTIC #' + str(self.id) + ': ' + str(self.text) + ']'

    def toDict(self):
        return {
            'text': self.text,
            'value': self.value,
            'datetime': self.datetime,
        }
