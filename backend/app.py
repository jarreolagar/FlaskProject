from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})#/blog/*

#Es la ruta que indica a que base de datos se va a conectar 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='root', server='localhost', database='aurora')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Esta clase es para crear el modelo de la tabla entradas, en base a esta clase, SQLAlchemy creará la tabla
class Entradas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text())
    articulo = db.Column(db.Text())
    fecha = db.Column(db.DateTime, default = datetime.datetime.now)

    #La variable fecha no se agrega al método __init_ porque esta declarada como default
    def __init__(self, titulo, articulo):
        self.titulo = titulo
        self.articulo = articulo
        
class EntradasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'titulo', 'articulo', 'fecha')

entrada_schema = EntradasSchema()
entradas_schema = EntradasSchema(many = True)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(15))
    contrasena = db.Column(db.String(10))

    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario', 'contrasena')

usuario_schema = EntradasSchema()
usuarios_schema = EntradasSchema(many = True)

@app.route('/leer_entrada', methods = ['GET'])
def obtener_entradas():
    #query.all() es un método de SQLAlchemy que hace un select al Schema especificado, es decir, a la tabla de la BD
    total_entradas = Entradas.query.all()
    resultado = entradas_schema.dump(total_entradas)
    return jsonify(resultado)



@app.route('/leer_entrada/<id>/', methods = ['GET'])
def obtener_id_entrada(id):
    entrada = Entradas.query.get(id)
    return entrada_schema.jsonify(entrada)



@app.route('/agregar_entrada', methods = ['POST'])
def agregar_entrada():
    titulo = request.json['titulo']
    articulo = request.json['articulo']

    entrada = Entradas(titulo, articulo)
    db.session.add(entrada)
    db.session.commit()
    #Se retorna con jsonify para que regrese el resultado como json, dentro de jsonify se pone el objeto entrada
    return entrada_schema.jsonify(entrada)



@app.route('/actualizar_entrada/<id>/', methods = ['PUT'])
def actualizar_entrada(id):
    entrada = Entradas.query.get(id)

    titulo = request.json['titulo']
    articulo = request.json['articulo']

    entrada.titulo = titulo
    entrada.articulo = articulo

    db.session.commit()
    return entrada_schema.jsonify(entrada)



@app.route('/eliminar_entrada/<id>/', methods = ['DELETE'])
def eliminar_entrada(id):
    entrada = Entradas.query.get(id)

    db.session.delete(entrada)
    db.session.commit()

    return entrada_schema.jsonify(entrada)



@app.route('/blog/mensaje/')
def mensaje():
    return jsonify("Obteniendo los datos desde Flask - Juan Arreola")

if __name__ == "__main__":
    app.run(debug=True)