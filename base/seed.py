from sqlalchemy.orm import Session
from models import Autor, Livro


def popular_banco(session: Session):
    a1 = Autor(nome="Machado de Assis")
    a2 = Autor(nome="Clarice Lispector")
    a3 = Autor(nome="George Orwell")

    session.add(a1)
    session.add_all([a2, a3])
    session.commit()

    livros = [
        Livro(titulo="Dom Casmurro", autor_id=a1.id, disponivel=True),
        Livro(
            titulo="Memórias Póstumas de Brás Cubas",
            autor_id=a1.id,
            disponivel=False,
        ),
        Livro(titulo="Quincas Borba", autor_id=a1.id, disponivel=True),
        Livro(titulo="A Hora da Estrela", autor_id=a2.id, disponivel=True),
        Livro(titulo="1984", autor_id=a3.id, disponivel=False),
        Livro(
            titulo="A Revolução dos Bichos",
            autor_id=a3.id,
            disponivel=True,
        ),
    ]

    session.add_all(livros)
    session.commit()