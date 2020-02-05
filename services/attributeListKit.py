from flask_restful import Resource, reqparse
from controllers.kit_c import KitController
from flask import jsonify

'''
    Clase encargada de responder solicitud REST a /api/attrlist/<string:uuid>
'''


class AttributeListKit(Resource):

    def __init__(self):
        self.controller = KitController()

    def get(self, uuid):
        kit = self.controller.find_by_uuid(uuid)
        if kit:
            entity_type = kit.entity_type
            if entity_type:
                attributes_list = entity_type.attributes
                result = [attr.json() for attr in attributes_list]
                return jsonify(result)
            else:
                return {'message': 'Kit dont have Entity Type'}, 404
        return {'message': 'Kit not found'}, 404


