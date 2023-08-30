import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'nave'
)
nome = "Conchinha"
login = "calvo"
senha = "123"

cursor = conexao.cursor()

#comando = "select *  from tb_login"
comando = 'insert into tb_login(nome,login,senha) values("{vnome}","{vlogin}","{vsenha}")'
cursor.execute(comando)

#resultado = cursor.fetchall()
conexao.commit()
print("cadastrado")