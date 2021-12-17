from flask import Flask
from config import Config

# importing blueprint
from .auth.routes import auth
from .blog.routes import blog

# importing database
from .models import db, User

# import database related
from flask_migrate import Migrate

# what we use to keep track of all of our logged in users
from flask_login import LoginManager


# instanciating Flask class
app = Flask(__name__)
login = LoginManager()


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)
app.register_blueprint(blog)

# setting configuration for Config class from config and variables in .env folder
app.config.from_object(Config)

# initialize database
db.init_app(app)
login.init_app(app)

migrate = Migrate(app,db)



# registering blueprint

from . import routes
from . import models
