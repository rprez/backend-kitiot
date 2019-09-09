from flask_restful import Resource, reqparse
from controllers.kit_c import KitController
from mongo import db
from pymongo import DESCENDING
from flask import Response
from bson.json_util import dumps
'''
    Clase encargada de gestionar las APIs Rest
'''


class LastMeasure(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('device_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('data_type',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('firmware_id',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('data',
                        type=list,
                        location='json',
                        required=True,
                        help="This field cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self,uuid):
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            message = db.data.find_one({'device_id': int(uuid)}, sort=[( '_id', DESCENDING)]);
            return Response(dumps(message),mimetype='application/json' ) if message else {}
        return {'message': 'Kit not found'}, 404