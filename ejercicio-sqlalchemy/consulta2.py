from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_
from generarTablas import Jugadores
engine = create_engine('sqlite:///jugadores.db')
Session = sessionmaker(bind=engine)
session = Session()

#jugadores, ordenados por la estatura
consulta2 = session.query(Jugadores).order_by(Jugadores.height.desc()).all()

for x in consulta2:
    print(x.first_name, x.height)
