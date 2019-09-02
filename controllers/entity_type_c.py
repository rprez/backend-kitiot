from models.entity_type import EntityType
from db import db


class EntityTypeController:

    def find_by_id(self,id) -> "EntityType":
        return db.session.query(EntityType).get(id)


