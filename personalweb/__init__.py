from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config.from_object('config.ProductionConfig')
db = SQLAlchemy(app) # conect db

from flask_bootstrap import Bootstrap
from personalweb.views import bp
from personalweb.project.views import project

bootstrap = Bootstrap(app)
app.register_blueprint(bp)
app.register_blueprint(project)

# Execute all cons
db.create_all()