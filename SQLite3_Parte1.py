# TESTE DE BANCO DE DADOS PARTE 1
import sqlite3 as SQLite
from time import sleep  # Apenas para uma visualização mais suave do processo no terminal.
import pandas as pd     # Apenas para uma visualização melhor da tabela no terminal.

# DICIONÁRIO PARA AJUDAR A ADICIONAR OS MESES
listaDeMeses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
                7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

# CRIA UM BANCO DE DADOS E UMA VARIÁVEL PARA O CURSOR, PARA EXECUTAR OS COMANDOS SQLite
banco = SQLite.connect("testeDATABSE.db"); print("Abrindo banco de dados...")
cursor = banco.cursor()

# VARIÁVEIS PARA USAR DE EXEMPLOS
vr_Nome = input("Digite um nome de uma pessoa: ")
vr_Idade = int(input("Digite uma idade: "))
vr_CPF = int(input("Digite uma sequência de 11 números para usar como exemplo de CPF(identidade): "))
vr_EstadoCivil = input("Digite o estado civil: ")
vr_Comentario = input("Digite um comentário: ")

# CRIANDO A TABELA
print(f"Criando tabela Pessoas..."); sleep(2)
cursor.execute(f""" CREATE TABLE IF NOT EXISTS Pessoas 
                    (
                    CPF             INTEGER         PRIMARY KEY,
                    Nome            TEXT            NOT NULL,
                    Idade           INTEGER,
                    Estado_Civil    TEXT,
                    Comentário      TEXT
                    )
            """)

# INSERINDO DADOS
print(f"Inserindo dados na tabela Pessoas..."); sleep(2)
cursor.execute(f""" INSERT INTO Pessoas VALUES 
                    (
                    '{vr_CPF}',
                    '{vr_Nome}',
                    '{vr_Idade}',
                    '{vr_EstadoCivil}',
                    '{vr_Comentario}'
                    )
            """)
banco.commit()

AUX = f""" SELECT * FROM Pessoas"""
df = pd.read_sql_query(AUX, banco)
print(df)

print("Fechando banco de dados..."); sleep(2)
banco.close()
