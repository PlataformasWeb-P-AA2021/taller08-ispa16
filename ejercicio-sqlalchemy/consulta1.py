from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_
from generarTablas import Jugadores
engine = create_engine('sqlite:///jugadores.db')
Session = sessionmaker(bind=engine)
session = Session()

#jugadoresvordenados por el número de goles.
consulta1 = session.query(Jugadores).order_by(Jugadores.goles.desc()).all()
for x in consulta1:
    print(x.first_name, x.goles)
