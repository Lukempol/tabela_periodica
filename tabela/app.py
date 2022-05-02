import tabela.database as database
import tabela.commands as commands
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tabela.model import Element
import unicodedata

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123@localhost:5432/periodic'
#app.config['DEVELOPMENT'] = True
database.init_app(app)
commands.init_app(app)

@app.route('/n/<n>')
def num_atomico(n: int):
    elemento = Element.query.filter_by(atomic_number=n).all()
    if len(elemento)==0:
        return 'Não encontrado', 404
    return f'{elemento[0].element_symbol}: {elemento[0].element_name}, n = {elemento[0].atomic_number}'
    
@app.route('/elemento/<nome>')
def nome_elemento(nome: str):
    
    if len(nome) < 3:
        nome = nome.capitalize()
        elemento = Element.query.filter_by(element_symbol=nome).all()
    else:
        #nome = unicodedata.normalize('NFD', nome).encode('ascii', 'ignore').decode('utf8').casefold() #Adicionar depois que acrescentar a coluna de nome sem acento no bd
        elemento = Element.query.filter_by(element_name=nome).all()
    
    if len(elemento)==0:
        return 'Não encontrado', 404
    return f'{elemento[0].element_symbol}: {elemento[0].element_name}, n = {elemento[0].atomic_number}'
 


if __name__ == '__main__':
    app.run()
