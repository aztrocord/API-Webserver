from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask_marshmallow import Marshmallow

app = Flask(__name__)