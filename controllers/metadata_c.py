from models.metadata import Metadata
from db import db


class MetadataController:

    def find_by_id(self,id) -> "Metadata":
        return db.session.query(Metadata).get(id)


