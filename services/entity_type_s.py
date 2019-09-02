from flask_restful import Resource
from controllers.entity_type_c import EntityTypeController

'''
    Clase encargada de gestionar las APIs Rest
'''


class EntityType(Resource):

    def __init__(self):
        self.controller = EntityTypeController()

    def get(self, id):
        entity_type = self.controller.find_by_id(id)
        if entity_type:
            return entity_type.json()
        return {'message': 'EntityType not found'}, 404



