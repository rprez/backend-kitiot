from models.kit import KitModel
from db import db

class KitController:

    @staticmethod
    def get_attributes_list() -> list:
        return ["name", "location","lat","long","context_id","device_id"]

    def find_by_id(self,id) -> "KitModel":
        return db.session.query(KitModel).get(id)

    def find_by_uuid(self,uuid) -> "KitModel":
        return db.session.query(KitModel).filter_by(uuid=uuid).first()

    def create_kit(self,uuid,name="",location="",lat=0.0,long=0.0):
        new_kit = KitModel(str(uuid),name,location,lat,long)
        return KitModel.save_to_db(new_kit)
