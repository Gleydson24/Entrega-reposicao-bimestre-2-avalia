from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Livro


def listar_livros(session: Session) -> List[Livro]:
    return list(session.scalars(select(Livro)).all())


def listar_livros_disponiveis(session: Session) -> List[Livro]:
    return list(
        session.scalars(select(Livro).where(Livro.disponivel == True)).all()
    )

def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.
    pass


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    pass
