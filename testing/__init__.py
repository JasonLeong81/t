from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
db.init_app(app)
from testing.routes import user

app.register_blueprint(user)
db.create_all()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    from testing.routes import user
    app.register_blueprint(user)
    return app