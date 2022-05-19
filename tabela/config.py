def init_app(app):
    app.config.update(
        SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:123@localhost:5432/periodic',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
