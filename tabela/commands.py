import click
from tabela.database import db
from tabela.model import Element
from tabela.elementos import tabela


def create_db():
    """Cria o banco de dados e a tabela"""
    db.create_all()


def drop_db():
    """Limpa o banco de dados"""
    db.drop_all()


def populate_db():
    """Adiciona os elementos a tabela"""
    commits = []
    for elemento in tabela:
        commits.append(
            Element(
                atomic_number=elemento.n,
                name=elemento.nome,
                symbol=elemento.simbolo,
                simple_name=elemento.nome_simples,
            )
        )
    db.session.add_all(commits)
    db.session.commit()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
