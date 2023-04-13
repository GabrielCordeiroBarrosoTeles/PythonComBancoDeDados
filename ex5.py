import mysql.connector
conexao =mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cordeiro'
)
cursor = conexao.cursor()

opcao = int(input("1-Cadastrar \n 2-Exibir\n 3-Pesquiasar por ID\n"))
match opcao:
    case 1:
        #Cadastro
        nome = input("Informe seu Nome:")
        sobrenome = input("Informe seu Sobrenome:")
        email = input("Informe seu E-mail:")
        nome_pai = input("Informe o Nome do Pai:")
        nome_mae = input("Informe o Nome da sua Mãe:")
        endereco = input("Informe seu Endereço:")
        telefone = int(input("Informe seu Telefone:"))
        comando1 = f'INSERT INTO aluno VALUES(0,"{nome}","{sobrenome}","{email}","{nome_pai}","{nome_mae}","{endereco}","{telefone}")'
        cursor.execute(comando1)
    case 2:
        #Exibir
        comando2 = 'SELECT * FROM aluno'
        cursor.execute(comando2)
        resultado = cursor.fetchall()
        print(resultado)
    case 3:
        n_id = int(input("Informe o ID que você deseja pesquisar:"))
        comando3 = f'SELECT*FROM aluno WHERE id="{n_id}"'
        cursor.execute(comando3)
        resultado = cursor.fetchall()
        print(resultado)

conexao.commit()
cursor.close()
conexao.close()
