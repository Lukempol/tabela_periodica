from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import tabela.database as database
import tabela.commands as commands
import tabela.resources as resources
import tabela.config as config

app = Flask(__name__)

config.init_app(app)
database.init_app(app)
commands.init_app(app)
resources.init_app(app)


if __name__ == "__main__":
    app.run()
