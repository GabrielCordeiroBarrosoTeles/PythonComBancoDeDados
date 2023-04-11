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
n_id = int(input("Informe o ID que você deseja pesquisar:"))

comando = f'SELECT*FROM aluno WHERE id="{n_id}"'


cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
conexao.commit()
cursor.close()
conexao.close()

