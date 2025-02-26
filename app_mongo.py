from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps  # Para serializar objetos BSON para JSON

app = Flask(__name__)

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['biblioteca']

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    usuario_id = db.usuarios.insert_one(data).inserted_id
    return jsonify({"mensagem": "Usuário criado com sucesso!", "id": str(usuario_id)}), 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = list(db.usuarios.find())
    return dumps(usuarios), 200  # Converte objetos BSON para JSON

@app.route('/livros', methods=['POST'])
def criar_livro():
    data = request.json
    livro_id = db.livros.insert_one(data).inserted_id
    return jsonify({"mensagem": "Livro criado com sucesso!", "id": str(livro_id)}), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = list(db.livros.find())
    return dumps(livros), 200

@app.route('/avaliacoes', methods=['POST'])
def criar_avaliacao():
    data = request.json
    # Adiciona a avaliação ao livro
    db.livros.update_one({"_id": ObjectId(data['livro_id'])}, {"$push": {"avaliacoes": data}})
    # Adiciona a avaliação ao usuário
    db.usuarios.update_one({"_id": ObjectId(data['usuario_id'])}, {"$push": {"livros_avaliados": data}})
    return jsonify({"mensagem": "Avaliação criada com sucesso!"}), 201

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo')
    livros = db.livros.find({"$or": [{"titulo": {"$regex": termo, "$options": "i"}}, {"genero": {"$regex": termo, "$options": "i"}}]})
    return dumps(livros), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)