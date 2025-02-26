Alunos: Vinícius Liam Almeida, Jonathan Candido Almeida Silva

O trabalho consiste em criar uma **API** utilizando o framework **Flask** para realizar operações de **inserção** e **consulta** de dados em dois bancos de dados diferentes: **PostgreSQL** (um banco de dados relacional) e **MongoDB** (um banco de dados NoSQL). Além disso, o objetivo é realizar **testes de desempenho** para comparar a eficiência de ambos os bancos de dados em termos de tempo de inserção e consulta de dados.

### Descrição Detalhada do Trabalho

#### 1. **API Flask**
A API Flask é desenvolvida para interagir com dois bancos de dados:
- **PostgreSQL**: Um banco de dados relacional que utiliza SQL para operações de inserção e consulta.
- **MongoDB**: Um banco de dados NoSQL que armazena dados em formato de documentos JSON (BSON).

A API possui endpoints para:
- **Criar usuários**: Inserir dados de usuários no banco de dados.
- **Criar livros**: Inserir dados de livros no banco de dados.
- **Criar avaliações**: Inserir avaliações de livros feitas por usuários.
- **Buscar livros**: Realizar consultas para buscar livros com base em um termo de pesquisa (título ou gênero).

#### 2. **Geração de Dados Fictícios**
Para realizar os testes de desempenho, são gerados dados fictícios utilizando a biblioteca **Faker**. Esses dados incluem:
- **Usuários**: Nome, e-mail e preferências.
- **Livros**: Título, autor, gênero e descrição.
- **Avaliações**: Nota e comentário, associando usuários e livros.

#### 3. **Testes de Desempenho**
Os testes de desempenho são realizados para comparar o tempo de execução das operações de **inserção** e **consulta** nos dois bancos de dados. O processo envolve:

A partir da biblioteca faker gerar 50 usuários, 800 livros e 2500 avaliações, que serão inseridos no **PostgreSQL e MongoDB**.

#### 4. **Comparação entre PostgreSQL e MongoDB**
O trabalho compara o desempenho dos dois bancos de dados, dando um print pelo terminal em termos de:
- **Tempo de inserção**: 
1. No PostgreSQL:

Print no terminal:![alt text](imagens/image.png)

2. No MongoDB:

Print no terminal:
![alt text](imagens/image-2.png)

- **Tempo de consulta**:

Print no terminal:![alt text](imagens/image-3.png)

2. No MongoDB:

Print no terminal:![alt text](imagens/image-5.png)

### Estrutura do Trabalho
1. **API Flask**:
   - Uma instância da API para PostgreSQL (rodando na porta 5000).
   - Uma instância da API para MongoDB (rodando na porta 5001).
2. **Script de Teste**:
   - Gera dados fictícios.
   - Realiza testes de inserção e consulta em ambos os bancos de dados.
   - Exibe os tempos de execução para comparação.

### Conclusão
A API desenvolvida com o Flask permitiu realizar uma comparação prática entre o PostgreSQL (banco de dados relacional) e o MongoDB (banco de dados NoSQL) em termos de desempenho para operações de inserção e consulta. Os resultados demonstram que o MongoDB apresenta um tempo de inserção e consulta significativamente menor em comparação ao PostgreSQL, especialmente quando se trata de grandes volumes de dados. Isso ocorre devido à natureza flexível e orientada a documentos do MongoDB, que otimiza operações de escrita e leitura em cenários onde a estrutura dos dados é mais dinâmica.

Por outro lado, o PostgreSQL, embora tenha um tempo de resposta um pouco maior, é altamente confiável e eficiente para consultas complexas e relacionamentos estruturados entre tabelas, características que são essenciais em aplicações que exigem consistência e integridade dos dados.

A escolha de qual tipo de Banco de Dados depende do projeto e da complexida do mesmo.