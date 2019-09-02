from db import db


class EntityType(db.Model):
    __tablename__ = "entity_type"

    id = db.Column(db.Integer, db.Sequence('id_seq_entity_type'), primary_key=True)
    name = db.Column('name', db.String(10))
    attributes = db.relationship("Attribute",backref='entity_type')


    def __init__(self, name) -> None:
        self.name = name

    def json(self):
        return {'id': self.id, 'name': self.name}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()