from flask_restful import Resource, reqparse
from controllers.kit_c import KitController
from mongo import db
from pymongo import DESCENDING
from flask import Response
from bson.json_util import dumps


class History(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('page_current',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )
    parser.add_argument('page_size',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        params = History.parser.parse_args()
        if params:
            kit = self.controller.find_by_uuid(uuid)
            if kit:
                skips = params.page_size * (params.page_current - 1) if params.page_current else 0
                message = db.data.find({'device_id': int(uuid)}, sort=[( '_id', DESCENDING)]).skip(skips).limit(params.page_size);
                return Response(dumps(message),mimetype='application/json') if message else {}
            return {'message': 'Kit not found'}, 404
        else:
            return {'message': 'Params: page_current and page_size cant be null'}, 400


class Total(Resource):

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            total = db.data.find({'device_id': int(uuid)}).count();
            return Response({"total":total},mimetype='application/json') if total else {"total":0}
        return {'message': 'Kit not found'}, 404

class Total(Resource):

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            total = db.data.find({'device_id': int(uuid)}).count();
            return Response(dumps({"total":total}),mimetype='application/json') if total else {"total":0}
        return {'message': 'Kit not found'}, 404