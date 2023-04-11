##pip install mysql-connector-python
import mysql.connector
conexao =mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cordeiro'
)
cursor = conexao.cursor()
#creat

nome = input("Informe seu Nome:")
sobrenome = input("Informe seu Sobrenome:")
email = input("Informe seu E-mail:")
nome_pai = input("Informe o Nome do Pai:")
nome_mae = input("Informe o Nome da sua Mãe:")
endereco = input("Informe seu Endereço:")
telefone = int(input("Informe seu Telefone:"))


comando1 = f'INSERT INTO aluno VALUES(0,"{nome}","{sobrenome}","{email}","{nome_pai}","{nome_mae}","{endereco}","{telefone}")'
comando2 = 'SELECT * FROM aluno'
cursor.execute(comando1)
cursor.execute(comando2)
resultado = cursor.fetchall()
print(resultado)
conexao.commit()
cursor.close()
conexao.close()

