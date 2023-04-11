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
comando = 'INSERT INTO aluno VALUES(0,"Gabriel","Cordeiro","gabriel@gmail.com","Tadeu","Claudia","De baixo da ponte","157")'
cursor.execute(comando)
conexao.commit()
cursor.close()
conexao.close()

