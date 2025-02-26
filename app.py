from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configurações do PostgreSQL
DATABASE_CONFIG = {
    'dbname': 'biblioteca',
    'user': 'vinicius',
    'password': '1234',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    conn.cursor_factory = RealDictCursor
    return conn

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Usuarios (nome, email, preferencias) VALUES (%s, %s, %s) RETURNING id',
        (data['nome'], data['email'], data['preferencias'])
    )
    usuario_id = cursor.fetchone()['id']
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Usuário criado com sucesso!", "id": usuario_id}), 201

@app.route('/livros', methods=['POST'])
def criar_livro():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Livros (titulo, autor, genero, descricao) VALUES (%s, %s, %s, %s) RETURNING id',
        (data['titulo'], data['autor'], data['genero'], data['descricao'])
    )
    livro_id = cursor.fetchone()['id']
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Livro criado com sucesso!", "id": livro_id}), 201

@app.route('/avaliacoes', methods=['POST'])
def criar_avaliacao():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Avaliacoes (usuario_id, livro_id, nota, comentario) VALUES (%s, %s, %s, %s) RETURNING id',
        (data['usuario_id'], data['livro_id'], data['nota'], data['comentario'])
    )
    avaliacao_id = cursor.fetchone()['id']
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Avaliação criada com sucesso!", "id": avaliacao_id}), 201

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM Livros WHERE titulo ILIKE %s OR genero ILIKE %s',
        (f'%{termo}%', f'%{termo}%')
    )
    livros = cursor.fetchall()
    conn.close()
    return jsonify(livros)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)