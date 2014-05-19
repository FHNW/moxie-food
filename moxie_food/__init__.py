from flask import Blueprint

from .views import FoodView


def create_blueprint(blueprint_name, conf):
    food_blueprint = Blueprint(blueprint_name, __name__, **conf)
    food_blueprint.add_url_rule('/', view_func=FoodView.as_view('food'))
    return food_blueprint
