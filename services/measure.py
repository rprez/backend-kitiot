from flask_restful import Resource, reqparse
from controllers.kit_c import KitController
from mongo import db

'''
    Clase encargada de gestionar las APIs Rest
'''


class Measure(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('device_id',
                        type=str,
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

    def post(self):
        data = Measure.parser.parse_args()
        if data:
            if data.device_id:
                kit = self.controller.find_by_uuid(str(data.device_id))
                if kit:
                    result = db.data.insert_one(data)
                    return ({'message': 'Measure save'}, 201) if result else ({'message': 'Measure not save in db'}, 500)
                return {'message': 'Device not found'}, 404
            else:
                return {'message': 'UUID empty'}, 400
        else:
            return {'message': 'Empty json'}, 400