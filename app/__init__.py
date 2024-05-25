from flask import Flask
from app.blueprints.user import userRoutes
from app.blueprints.web import webRoutes
from app.models import db
import app.models.user

app = Flask(__name__)
app.register_blueprint(userRoutes)
app.register_blueprint(webRoutes)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
with app.app_context():
    db.create_all()
