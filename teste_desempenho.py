import time
from faker import Faker
import requests

fake = Faker()

# Gerar dados fictícios
def gerar_dados_ficticios(num_usuarios=50, num_livros=800, num_avaliacoes=2500):
    usuarios = [{"nome": fake.name(), "email": fake.email(), "preferencias": fake.words(nb=3)} for _ in range(num_usuarios)]
    livros = [{"titulo": fake.sentence(), "autor": fake.name(), "genero": fake.word(), "descricao": fake.text()} for _ in range(num_livros)]
    avaliacoes = [{"usuario_id": fake.random_int(min=1, max=num_usuarios), "livro_id": fake.random_int(min=1, max=num_livros), "nota": fake.random_int(min=1, max=5), "comentario": fake.text()} for _ in range(num_avaliacoes)]
    return usuarios, livros, avaliacoes

# Teste de desempenho para PostgreSQL
def testar_postgresql():
    usuarios, livros, avaliacoes = gerar_dados_ficticios()
    
    start_time = time.time()
    
    for usuario in usuarios:
        requests.post('http://127.0.0.1:5000/usuarios', json=usuario)
    
    for livro in livros:
        requests.post('http://127.0.0.1:5000/livros', json=livro)
    
    for avaliacao in avaliacoes:
        requests.post('http://127.0.0.1:5000/avaliacoes', json=avaliacao)
    
    end_time = time.time()
    print(f"Tempo de inserção PostgreSQL: {end_time - start_time} segundos")
    
    start_time = time.time()
    requests.get('http://127.0.0.1:5000/buscar?termo=Ficção')
    end_time = time.time()
    print(f"Tempo de consulta PostgreSQL: {end_time - start_time} segundos")

# Teste de desempenho para MongoDB
def testar_mongodb():
    usuarios, livros, avaliacoes = gerar_dados_ficticios()
    
    start_time = time.time()
    
    for usuario in usuarios:
        requests.post('http://127.0.0.1:5001/usuarios', json=usuario)
    
    for livro in livros:
        requests.post('http://127.0.0.1:5001/livros', json=livro)
    
    for avaliacao in avaliacoes:
        requests.post('http://127.0.0.1:5001/avaliacoes', json=avaliacao)
    
    end_time = time.time()
    print(f"Tempo de inserção MongoDB: {end_time - start_time} segundos")
    
    start_time = time.time()
    requests.get('http://127.0.0.1:5001/buscar?termo=Ficção')
    end_time = time.time()
    print(f"Tempo de consulta MongoDB: {end_time - start_time} segundos")

if __name__ == '__main__':
    testar_postgresql()
    testar_mongodb()