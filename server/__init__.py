from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .commands import create_tables
from .routes import main
from .admin_actions.branch.routes import branch
from ..server.user_actions.billing.zones.routes import zones
from ..server.user_actions.billing.zones.destinations.routes import destination
from ..server.user_actions.billing.weight.routes import weight


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    migrate = Migrate(app, db)

    #Routes for module ...
    app.register_blueprint(main)
    app.register_blueprint(branch)
    app.register_blueprint(destination)
    app.register_blueprint(zones)
    app.register_blueprint(weight)

    app.cli.add_command(create_tables)
    return app
