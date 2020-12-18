from flask_restful import Resource
from controllers.kit_c import KitController
from mongo import db
from pymongo import DESCENDING
from flask import Response
from bson.json_util import dumps
'''
    Clase encargada de gestionar las APIs Rest
'''


class LastMeasure(Resource):

    def __init__(self):
        self.controller = KitController()

    def get(self,uuid):
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            message = db.data.find({'device_id': uuid},{'_id':0}, sort=[( '_id', DESCENDING)])[0:2];
            return Response(dumps(message),mimetype='application/json' ) if message else {}
        return {'message': 'Kit not found'}, 404