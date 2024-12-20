import os
from flask import Flask, render_template

from blueprints.ui import app as ui_app
from blueprints.service import app as service_app
from blueprints.statistic import app as statistic_app
from middleware import Middleware
from utils.utils import read_config

_config = read_config('config.json')


app = Flask(__name__)
app.wsgi_app = Middleware(app.wsgi_app, url_prefix='/api', cors_origins=_config['cors-origins'])

app.register_blueprint(ui_app, url_prefix='/ui')
app.register_blueprint(service_app, url_prefix='/service')
app.register_blueprint(statistic_app, url_prefix='/statistic')

@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(404)
def error404(err):
    print(err)
    return "404 страница не найдена"


@app.errorhandler(500)
def error500(err):
    print(err)
    return "500 внутренняя ошибка сервера"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', _config['api_port']))
    host = _config['api_host']
    app.run(port=port, debug=bool(_config['debug']), host=host)
