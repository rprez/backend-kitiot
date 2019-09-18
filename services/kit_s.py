from flask_restful import Resource, reqparse
from controllers.kit_c import KitController

'''
    Clase encargada de gestionar las APIs Rest
'''


class Kit(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('name',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('location',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('lat',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('long',
                        type=float,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('installation_date',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            return kit.json()
        return {'message': 'Kit not found'}, 404


    def post(self,uuid):
        data = Kit.parser.parse_args()
        if data:
            new_kit = self.controller.create_kit(data.uuid,data.name,data.location,data.lat,data.long,data.installation_date)
            if new_kit:
                return {'message': 'Kit create'}, 201
            else:
                return {'message': 'Kit could not be create'}, 500
        return {'message': 'Meassure empty'}, 404


