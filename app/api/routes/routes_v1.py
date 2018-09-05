from sanic import Blueprint
from app.api.v1.views.cart_view import UserView

api_v1_blueprint = Blueprint('api.v1', url_prefix='/api/v1')
api_v1_blueprint.route(
    '/user', methods=["GET", "POST", "PUT", "DELETE"])(UserView.as_view())
