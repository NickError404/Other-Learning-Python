import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = conexao.cursor()

# cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100)) ;')
# cursor.execute('create table teste(nome varchar(30));')

nome = str(input('Digite seu endereço: ')).strip()
endereço = str(input('Digite seu endereço: ')).strip()
with conexao.cursor() as cursor:
    cursor.execute(f'insert into cadastros(nome, endereco) values ("{nome}", "{endereço}")')
    conexao.commit()

# with conexao.cursor() as cursor:
#     cursor.execute('create table cadastros( id int primary key auto_increment, nome varchar(50) not null, endereco varchar(300));')
#     conexao.commit()

cursor.close()
conexao.close()
