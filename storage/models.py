from utils.utils import read_config

config = read_config('config.json')


class Service:
    token: str
    write_token: str
    js_parser_code: str
    name: str

    def __init__(self, token, write_token, name, js_parser_code, registered):
        self.write_token = write_token
        self.token = token
        self.name = name
        self.js_parser_code = js_parser_code
        self.registered = registered

    def __repr__(self):
        return '[SERVICE #' + str(self.name) + ']'

    def toDict(self, private: bool):
        return {
            'token': self.token,
            'write_token': self.write_token,
            'js_parser_code': self.js_parser_code,
            'name': self.name,
            'registered': self.registered,
        } if private else {
            'name': self.name,
            'registered': self.registered,
        }


class Statistic:
    id: int
    service_token: str
    text: str
    value: float
    boolean: bool
    datetime: str

    def __init__(self, id: int, service_token: str, text: str, value: float, boolean: bool, datetime: str):
        self.id = id
        self.service_token = service_token
        self.text = text
        self.value = value
        self.boolean = boolean
        self.datetime = datetime

    def __repr__(self):
        return '[STATISTIC #' + str(self.id) + ': ' + str(self.text) + ']'

    def toDict(self):
        return {
            'id': self.id,
            'text': self.text,
            'value': self.value,
            'bool': self.boolean,
            'datetime': self.datetime,
        }
