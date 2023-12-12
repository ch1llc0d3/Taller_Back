from flask import Flask, render_template, request
from modelos import db, Heroe

#Instancia de la clase Flask de la biblioteca flask. 
app = Flask(__name__)

# Configuramos la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializar la db
db.init_app(app)

### RUTAS ###

# Ruta principal - Ver heroes
@app.route('/')
def index():

# Traemos todos los heroes de la base de datos
    heroes = Heroe.query.all()

    return render_template("index.html", heroes=heroes)





### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)