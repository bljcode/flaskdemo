from flask import Blueprint

main = Blueprint('main',__name__)
# import view
from . import view,errors,strategy

