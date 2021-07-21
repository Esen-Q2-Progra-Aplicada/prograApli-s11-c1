from flask import render_template
from logic.client_logic import ClientLogic


class MainRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/")
        def home():
            logic = ClientLogic()
            clientList = logic.getAll()
            return render_template("index.html", clients=clientList)
