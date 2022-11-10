from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee':'haw'}

@api.route('/contacts',methods=['POST'])
@token_required
def create_contact(current_user):
    name = request.json['name']
    email = request.json



