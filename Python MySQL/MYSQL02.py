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

nome = str(input('Digite seu endereço: ')).strip()
endereço = str(input('Digite seu endereço: ')).strip()
with conexao.cursor() as cursor:
    cursor.execute(f'insert into cadastros(nome, endereco) values ("{nome}", "{endereço}")')
    conexao.commit()

