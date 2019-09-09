from app import server
from db import db

db.init_app(server)

@server.before_first_request
def create_tables():
    db.create_all()