from flask import Blueprint

from ...extensions import db


main = Blueprint('main', __name__, template_folder="templates")


@main.route('/')
def index():
    return "<h1>Hello world!</h1>"
