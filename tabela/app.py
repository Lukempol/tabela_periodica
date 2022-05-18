from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import tabela.database as database
import tabela.commands as commands
import tabela.resources as resources


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:123@localhost:5432/periodic"
# app.config['DEVELOPMENT'] = True
database.init_app(app)
commands.init_app(app)
resources.init_app(app)


if __name__ == "__main__":
    app.run()
