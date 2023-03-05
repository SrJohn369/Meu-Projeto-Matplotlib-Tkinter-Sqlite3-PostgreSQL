import psycopg2 as post


# Conectando a um database existente
# Verificando erros
try:
    # Geralmente quando se cria um servidor postgres é, por padrão, criado um DB com nome postgres
    banco = post.connect("dbname=testPython user=postgres password=postgres host=localhost port=5432")
except post.OperationalError as err:
    print('Erro ao conectar ao banco', err)
# Criar um cursor para fazer os códigos postgres
cur = banco.cursor()

try:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS testPython 
        (
            primeiro_nome       VARCHAR(30),
            ultimo_nome         VARCHAR(30),
            data_nascimento     DATE
        );
    """)
    banco.commit() # Sempre lembrar de fazer commit, caso contrário nada acontecerá
except post.OperationalError as err:
    print("erro ao criar tabela", err)
