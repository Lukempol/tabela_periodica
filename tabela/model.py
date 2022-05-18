from tabela.database import db


class Element(db.Model):
    atomic_number = db.Column(db.SmallInteger, primary_key=True)
    # atomic_mass = db.Column(db.Float, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    symbol = db.Column(db.String(2), unique=True, nullable=False)
    simple_name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return "<Element %r>" % self.element_name
