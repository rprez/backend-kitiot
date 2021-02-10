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
                skips = params.page_size * (params.page_current)
                message = db.data.find({'device_id': int(uuid)}, {'_id':0}, sort=[( '_id', DESCENDING)]).skip(skips).limit(params.page_size);
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
            total = db.data.find({'device_id': uuid},{'_id':0}).count()
            return Response(dumps({"total":total}),mimetype='application/json') if total else {"total":0}
        return {'message': 'Kit not found'}, 404


class Measurement(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('start',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )
    parser.add_argument('end',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )
    parser.add_argument('param',
                        location='args',
                        type=str,
                        required=True,
                        help="This argument cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        params = Measurement.parser.parse_args()
        if params:
            kit = self.controller.find_by_uuid(uuid)
            if kit:
                pipeline = [
                    {"$match": {'device_id': uuid}},
                    {"$unwind": {'path': "$data"}},
                    {"$match": {'data.type_id': params.param,
                                'data.data.timestamp': {'$gte': params.start, '$lte': params.end}
                                }
                     },
                    {"$project": {"_id":0,"firmware_id":0}},
                    {"$sort": {'data.data.timestamp': -1}}
                ]
                query = list(db.data.aggregate(pipeline))
                datas = [element.get('data').get('data')[0].get('value') for element in query if element.get('data') and element.get('data').get('data')[0] ]
                tss = [element.get('data').get('data')[0].get('timestamp') for element in query if element.get('data') and element.get('data').get('data')[0] ]

                return Response(dumps({'data':datas, 'timestamps': tss}) , mimetype='application/json') if query else {}
            return {'message': 'Kit not found'}, 404
        else:
            return {'message': 'Params: from , to and param cant be null'}, 404


class Graph(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('start',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )
    parser.add_argument('end',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )
    parser.add_argument('param',
                        location='args',
                        type=str,
                        required=True,
                        help="This argument cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        params = Measurement.parser.parse_args()
        if params:
            kit = self.controller.find_by_uuid(uuid)
            if kit:
                pipeline = [
                    {"$match": {'device_id': uuid}},
                    {"$unwind": {'path': "$data"}},
                    {"$match": {'data.type_id': params.param,
                                'data.data.timestamp': {'$gte': params.start, '$lte': params.end}
                                }
                     },
                    {"$project": {"_id":0,"firmware_id":0}},
                    {"$sort": {'data.data.timestamp': -1}}
                ]
                query = list(db.data.aggregate(pipeline))
                datas = [[element.get('data').get('data')[0].get('value'),int(element.get('data').get('data')[0].get('timestamp'))*1000] for element in query if element.get('data') and element.get('data').get('data')[0] ]

                return Response(dumps({'data':datas}) , mimetype='application/json') if query else {}
            return {'message': 'Kit not found'}, 404
        else:
            return {'message': 'Params: from , to and param cant be null'}, 404