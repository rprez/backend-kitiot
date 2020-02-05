from db import db
from sqlalchemy.exc import IntegrityError

class KitModel(db.Model):
    __tablename__ = "kit"

    id = db.Column(db.Integer,db.Sequence('id_seq_kit'), primary_key=True)
    uuid = db.Column('uuid',db.String(20),unique=True)
    name = db.Column('name',db.String(15))
    location = db.Column('location', db.String(25))
    lat = db.Column('lat', db.Float)
    long = db.Column('long', db.Float)
    context_id = db.Column('context_id',db.String(25))
    device_id = db.Column('device_id', db.String(25))
    installation_date = db.Column('installation_date', db.DateTime)
    entity_type = db.relationship("EntityType",backref="kit")
    entity_type_id = db.Column(db.Integer, db.ForeignKey("entity_type.id"))

    def __init__(self, uuid, name, location, lat, long,installation_date, context_id='', device_id='',) -> None:
        self.uuid = uuid
        self.name = name
        self.location = location
        self.lat = lat
        self.long = long
        self.installation_date = installation_date
        self.context_id = context_id
        self.device_id = device_id


    def json(self):
        return {'id': self.id, 'uuid':self.uuid, 'name': self.name, 'location': self.location, 'lat': self.lat,
                'long': self.long, 'context_id': self.context_id, 'device_id':self.device_id, 'installation_date':str(self.installation_date)
        }

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except  IntegrityError as ex:
            db.session.rollback()
            return None
        return self

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()