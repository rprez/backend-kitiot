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
from services.history import History, Total,Measurement
from services.data import Search, SearchTotal

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
api.add_resource(Measure, '/data/measure')
api.add_resource(LastMeasure, '/data/last_measure/<string:uuid>')
api.add_resource(History, '/data/history/<string:uuid>',endpoint="history")
api.add_resource(Total, '/data/history/total/<string:uuid>',endpoint="total")
api.add_resource(Measurement, '/data/measurement/<string:uuid>',endpoint="measurement")
api.add_resource(Search, '/data/search/<string:uuid>',endpoint="search")
api.add_resource(SearchTotal, '/data/search/total/<string:uuid>',endpoint="search_total")

if __name__ == '__main__':
    from db import db

    if server.config['DEBUG']:
        @server.before_first_request
        def create_tables():
            print("Creating DataBase")
            db.create_all()

    db.init_app(server)
    server.run(port=5000)