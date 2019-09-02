from models.attribute import Attribute
from db import db


class AttributeController:

    def find_by_id(self,id) -> "Attribute":
        return db.session.query(Attribute).get(id)


