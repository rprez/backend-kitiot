from db import db


class Attribute(db.Model):
    __tablename__ = "attribute"

    id = db.Column(db.Integer, db.Sequence('id_seq_attribute'), primary_key=True)
    name = db.Column('name', db.String(25))
    type = db.Column('type', db.String(25))
    platform_name = db.Column('platform_name', db.String(10))
    entity_type_id = db.Column(db.Integer, db.ForeignKey("entity_type.id"))
    metadata_sensor = db.relationship("Metadata",backref='attribute')

    def __init__(self, name, type,platform_name):
        self.name = name
        self.type = type
        self.platform_name = platform_name

    def json(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'platform_name': self.platform_name}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()