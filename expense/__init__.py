from flask import Flask, Blueprint
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv


load_dotenv()
mongo = PyMongo()
jwt = JWTManager()
api = Api()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    mongo.init_app(app)
    jwt.init_app(app)

    # Create a Blueprint with the desired prefix
    main_bp = Blueprint('main', __name__, url_prefix='/api')

    # Initialize Flask-RESTful API with the Blueprint
    api.init_app(main_bp)

    # Initialize Flask-Marshmallow
    ma.init_app(app)

    # Import and register your resources/views here
    from .views import RegisterView, LoginView, ExpenseView, ExpenseListCreateView

    api.add_resource(RegisterView, '/register')
    api.add_resource(LoginView, '/login')
    api.add_resource(ExpenseListCreateView, '/expenses')
    api.add_resource(ExpenseView, '/expenses/<id>')

    # Register the Blueprint in your Flask application
    app.register_blueprint(main_bp)

    return app
