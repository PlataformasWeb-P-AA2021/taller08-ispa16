from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generarTablas import Jugadores
import csv

engine = create_engine('sqlite:///jugadores.db')

Session = sessionmaker(bind=engine)
session = Session()
#leer archivos
archivo = open('data/mundial2018.csv', 'r', encoding='utf-8')
archivo_csv = csv.reader(archivo, delimiter='|')
next(archivo_csv)
#crear objeto e ingresar datos
for d in archivo_csv:
    d = Jugadores(numero=int(d[0]), fifa_name=d[1], country=d[2], last_name=d[3], first_name=d[4], shirt_name=d[5],
             pos=d[6], height=int(d[7]), caps=int(d[8]), goles=int(d[9]))
    session.add(d)
session.commit()
