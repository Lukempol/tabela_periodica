from tabela.model import Element
import unicodedata


def init_app(app):
    @app.route("/n/<n>")
    def num_atomico(n: int):
        elemento = Element.query.filter_by(atomic_number=n).all()
        if len(elemento) == 0:
            return "Não encontrado", 404
        elemento = elemento[0]
        return f"{elemento.symbol}: {elemento.name}, n = {elemento.atomic_number}"

    @app.route("/elemento/<nome>")
    def nome_elemento(nome: str):

        if len(nome) < 3:
            nome = nome.capitalize()
            elemento = Element.query.filter_by(element_symbol=nome).all()
        else:
            nome = (
                unicodedata.normalize("NFD", nome)
                .encode("ascii", "ignore")
                .decode("utf8")
                .casefold()
            )
            elemento = Element.query.filter_by(simple_name=nome).all()

        if len(elemento) == 0:
            return "Não encontrado", 404
        elemento = elemento[0]
        return f"{elemento.symbol}: {elemento.name}, n = {elemento.atomic_number}"
