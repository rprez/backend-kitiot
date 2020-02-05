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
from services.attributeListKit import AttributeListKit
from flask_cors import CORS

server = flask.Flask(__name__)

server.config['DEBUG'] = True

server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.secret_key = '3b4be1bd-c4a3-x89d-nvft-1ac7a5de6c8c'
api = Api(server)
CORS(server,resources={r"/api/*": {"origins": "192.168.104.128:3000"}})

@server.route('/')
def index():
    return 'Hi - Rest OK'


api.add_resource(Kit, '/api/kit/<string:uuid>')
api.add_resource(AttributeListKit, '/api/attrlist/<string:uuid>')
api.add_resource(Attribute, '/api/attr/<string:id>')
api.add_resource(EntityType, '/api/entity_type/<string:id>')
api.add_resource(Metadata, '/api/metadata/<string:id>')
api.add_resource(Measure, '/api/data/measure')
api.add_resource(LastMeasure, '/api/data/last_measure/<string:uuid>')
api.add_resource(History, '/api/data/history/<string:uuid>',endpoint="history")
api.add_resource(Total, '/api/data/history/total/<string:uuid>',endpoint="total")
api.add_resource(Measurement, '/api/data/measurement/<string:uuid>',endpoint="measurement")
api.add_resource(Search, '/api/data/search/<string:uuid>',endpoint="search")
api.add_resource(SearchTotal, '/api/data/search/total/<string:uuid>',endpoint="search_total")

if __name__ == '__main__':
    from db import db

    if server.config['DEBUG']:
        @server.before_first_request
        def create_tables():
            print("Creating DataBase")
            db.create_all()

    db.init_app(server)
    server.run(host='0.0.0.0',port=5000)