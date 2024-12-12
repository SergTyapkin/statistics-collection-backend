from flask import Blueprint, request, render_template, redirect

from storage.storage import getAllServices, getServiceStatistics, getService
from utils.utils import time_prettify

app = Blueprint('ui', __name__)


@app.route("", methods=["GET"])
def uiDefault():
    return redirect('/')


@app.route("/service/all", methods=["GET"])
def uiServiceAll():
    services = getAllServices()
    for s in services:
        s.registered = time_prettify(s.registered)
    return render_template('service-all.html', services=services)

@app.route("/service/create", methods=["GET"])
def uiServiceCreate():
    return render_template('service-create.html')


@app.route("/service/delete", methods=["GET"])
def uiServiceDelete():
    return render_template('service-delete.html')


@app.route("/statistic/all", methods=["GET"])
def uiStatisticGetAll():
    try:
        req = request.args
        service_token = req['token']
    except:
        return redirect('/')

    service = getService(service_token)
    if not service:
        return redirect('/')

    statistics = getServiceStatistics(service.write_token)
    for s in statistics:
        s.datetime = time_prettify(s.datetime)
    return render_template('statistic-all.html', statistics=statistics, service=service)

@app.route("/statistic/delete", methods=["GET"])
def uiStatisticDelete():
    return render_template('statistic-delete.html')

@app.route("/statistic/create", methods=["GET"])
def uiStatisticCreate():
    return render_template('statistic-create.html')
