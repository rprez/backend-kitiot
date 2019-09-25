from flask_restful import Resource, reqparse
from controllers.kit_c import KitController
from mongo import db
from flask import Response
from bson.json_util import dumps

class Search(Resource):

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
    parser.add_argument('start',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        params = Search.parser.parse_args()
        if params:
            kit = self.controller.find_by_uuid(uuid)
            if kit:
                skips = params.page_size * (params.page_current)

                pipeline = [
                    {"$match": {'device_id': int(uuid)}},
                    {"$match": {
                            'data.data.timestamp': {'$gte': params.start}
                            }
                     },
                    {"$project": {"_id": 0}},
                    {"$sort": {'data.data.timestamp': -1}},
                    {"$skip": skips},
                    {"$limit": params.page_size}
                ]
                query = list(db.data.aggregate(pipeline))
                return Response(dumps(query),mimetype='application/json') if query else {}
            return {'message': 'Kit not found'}, 404
        else:
            return {'message': 'Params: page_current and page_size cant be null'}, 400


class SearchTotal(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('start',
                        location='args',
                        type=int,
                        required=True,
                        help="This argument cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        params = SearchTotal.parser.parse_args()
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            pipeline = [
                    {"$match": {'device_id': int(uuid)}},
                    {"$match": {
                            'data.data.timestamp': {'$gte': params.start}
                            }
                     },
                    {"$project": {"_id": 0}},
                    {"$count": 'records'}
            ]

            query = list(db.data.aggregate(pipeline))
            return Response(dumps({"total":query}),mimetype='application/json') if query else {"total":0}
        return {'message': 'Kit not found'}, 404
