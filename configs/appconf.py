import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

connex_app = connexion.App(__name__)

app = connex_app.app

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123@10.11.17.40/pet'

db = SQLAlchemy(app)

ma = Marshmallow(app)
