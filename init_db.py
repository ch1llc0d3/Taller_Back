from modelos import db, Heroe
from flask import Flask

#Instancia de la clase Flask de la biblioteca flask. 
app = Flask(__name__)

# Configuramos la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Crear tabla en la base de datos
# with app.app_context():
#     db.create_all()

# Cargamos los datos en la base de datos
with app.app_context():

    ### HEROES ###

    # Cargamos el primer heroe
    heroe_1 = Heroe(nombre='Iron Man', 
    apodo='Genio, millonario, playboy, filantropo', 
    edad=35, detalles='Lider de los Vengadores, fundador de Stark Industries', 
    foto='/static/ironman.png')

    # Cargamos el 2ndo heroe
    heroe_2 = Heroe(nombre='Chapulin Colorado', 
    apodo='Chapulin', 
    edad=50, detalles='El heroe mas simpatico', 
    foto='/static/chapulin.png')

    # Cargamos el 2ndo heroe
    heroe_3 = Heroe(nombre='Hulk', 
    apodo='Doc Green', 
    edad=35, detalles='Dr Bruce Banner', 
    foto='/static/hulk.png')

    # Cargamos el 2ndo heroe
    heroe_4 = Heroe(nombre='Nightwing', 
    apodo='Ex Robin', 
    edad=35, detalles='Ayudante de Batman', 
    foto='/static/nightwing.png')

    ### Agregar a la base de datos ###
    #db.session.add(heroe_1)
    db.session.add(heroe_2)
    db.session.add(heroe_3)
    db.session.add(heroe_4)

    # Guardar los cambios
    db.session.commit()
    

