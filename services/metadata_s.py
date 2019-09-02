from flask_restful import Resource
from controllers.metadata_c import MetadataController

'''
    Clase encargada de gestionar las APIs Rest
'''


class Metadata(Resource):

    def __init__(self):
        self.controller = MetadataController()

    def get(self, id):
        metadata = self.controller.find_by_id(id)
        if metadata:
            return metadata.json()
        return {'message': 'Metadata not found'}, 404



