from flask import Blueprint, request,jsonify,render_template
from helpers import taken_required
from models import db,User,Contact,contact_schema,contacts_schema

api = Blueprint('api',__name__,url_prefix='/api')
