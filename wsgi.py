from app import server
from db import db
from flask_cors import CORS

db.init_app(server)

CORS(server,resources={r"/api/*": {"origins": "http://179.27.167.3:3000"}})

@server.before_first_request
def create_tables():
    db.create_all()