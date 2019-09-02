from db import db

class Metadata(db.Model):
    __tablename__ = "metadata"

    id = db.Column(db.Integer, db.Sequence('id_seq_metadata'), primary_key=True)
    name = db.Column('name', db.String(10))
    type = db.Column('type', db.String(10))
    attribute_id = db.Column(db.Integer, db.ForeignKey("attribute.id"),nullable=False)

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def json(self):
        return {'id': self.id, 'name': self.name, 'type': self.type}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()