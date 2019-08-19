from flask import Flask, g
from werkzeug.utils import find_modules, import_string

from nexus.database import db, init_db

APP_NAME='Nexus'


def create_app(config=None):
    app = Flask(APP_NAME)

    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI='sqlite:///%s.db' % APP_NAME,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True,
        SECRET_KEY=b'super_secret_key',
    ))
    app.config.update(config or {})
    app.config.from_envvar('NEXUS_WEBAPP_SETTINGS', silent=True)

    register_blueprints(app)
    register_cli(app)
    register_teardowns(app)

    db.init_app(app)

    return app


def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('nexus.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app):
    # @app.cli.command('initdb')
    # def initdb_command():
    #     """Create database tables."""
    #     init_db()
    #     print('Initialized the database.')
    pass


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, '_database'):
            g.sqlite_db.close()
