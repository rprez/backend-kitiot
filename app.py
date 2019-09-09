# coding=utf-8
import flask
import os
from flask_restful import Api
from services.kit_s import Kit
from services.entity_type_s import EntityType
from services.attribute_s import Attribute
from services.metadata_s import Metadata
from services.measure import Measure
from services.last_measure import LastMeasure

server = flask.Flask(__name__)

server.config['DEBUG'] = True

server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.secret_key = '3b4be1bd-c8a8-479d-nvft-1ac7a5de6c8c'
api = Api(server)

@server.route('/')
def index():
    return 'Hi - Rest Api'

api.add_resource(Kit, '/kit/<string:uuid>')
api.add_resource(Attribute, '/attr/<string:id>')
api.add_resource(EntityType, '/entity_type/<string:id>')
api.add_resource(Metadata, '/metadata/<string:id>')
api.add_resource(Measure, '/measure')
api.add_resource(LastMeasure, '/last_measure/<string:uuid>')

if __name__ == '__main__':
    from db import db

    if server.config['DEBUG']:
        @server.before_first_request
        def create_tables():
            print("Creating DataBase")
            db.create_all()

    db.init_app(server)
    server.run(port=5000)