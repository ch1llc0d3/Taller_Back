# Creamos una tabla en la base de datos llamada "personas" con dos columnas: nombre y apellido
from flask_sqlalchemy import SQLAlchemy

# Crear objeto SQLAlchemy
db = SQLAlchemy()

### MODELOS ###


# Creamos el modelo de la tabla Heroe
class Heroe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30), nullable = False)
    apodo = db.Column(db.String(30), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    detalles = db.Column(db.String(30), nullable = False)
    foto = db.Column(db.String(30), nullable = False)



