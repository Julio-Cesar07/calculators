from flask import Flask
from src.main.routes.calculators import calc_route_pb

app = Flask(__name__)

app.register_blueprint(calc_route_pb)