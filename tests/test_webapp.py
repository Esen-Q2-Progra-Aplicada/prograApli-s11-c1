from flask import Flask
from routes.main_routes import MainRoutes
from logic.client_logic import ClientLogic
import requests


def test_webapp():
    assert True is True


def test_class_client_getall():
    logic = ClientLogic()
    clients = logic.getAll()
    assert len(clients) > 0
    assert "balbino" in clients
    assert clients == ["balbino", "rodrigo", "sofia", "patrica"]


def test_webapp_site_home():
    app = Flask(__name__, template_folder="../templates")
    MainRoutes.configure_routes(app)
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert b"this is my main page" in response.data


def test_webapp_clients_inpage():
    app = Flask(__name__, template_folder="../templates")
    MainRoutes.configure_routes(app)
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert b"balbino" in response.data
    assert b"patrica" in response.data
