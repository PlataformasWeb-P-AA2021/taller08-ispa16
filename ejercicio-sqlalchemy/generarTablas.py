from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///jugadores.db')

Base = declarative_base()


class Jugadores(Base):
    __tablename__ = "Mundial"
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fifa_name = Column(String(50))
    country = Column(String(50))
    last_name = Column(String(50))
    first_name = Column(String(50))
    shirt_name = Column(String(50))
    pos = Column(String(5))
    height = Column(Integer)
    caps = Column(Integer)
    goles = Column(Integer)



Base.metadata.create_all(engine)
