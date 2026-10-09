from typing import List

from sqlalchemy import ForeignKey, String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))

    livros: Mapped[List["Livro"]] = relationship("Livro", back_populates="autor")


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150))
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    disponivel: Mapped[bool] = mapped_column(default=True)

    autor: Mapped["Autor"] = relationship("Autor", back_populates="livros")