from flask_restful import Resource
from controllers.attribute_c import AttributeController

'''
    Clase encargada de gestionar las APIs Rest 
'''


class Attribute(Resource):

    def __init__(self):
        self.controller = AttributeController()

    def get(self, id):
        attribute = self.controller.find_by_id(id)
        if attribute:
            return attribute.json()
        return {'message': 'Attribute not found'}, 404



