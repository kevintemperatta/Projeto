from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column('id_usuario', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)

    def __init__(self, id,  nome):
        self.id = id
        self.nome = nome