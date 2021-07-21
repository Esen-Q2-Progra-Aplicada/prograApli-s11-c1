from flask import Flask
from routes.main_routes import MainRoutes
import requests


def test_webapp():
    assert True is True


def test_webapp_site_home():
    app = Flask(__name__, template_folder="../templates")
    MainRoutes.configure_routes(app)
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 404
    assert b"this is my main page" in response.data
