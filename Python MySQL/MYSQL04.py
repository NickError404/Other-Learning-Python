import pymysql.cursors

conexão = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

autenticado = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome =input('Digite seu nome: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                print('\033[1;32mAutenticado com sucesso!')
                break
            else:
                autenticado = False
        if not autenticado:
            print('\033[1;31mEmail ou Senha errado!')
    elif decisao == 2:
        print('\033[1;33mFaça seu cadastro!')
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('\033[31;3mUsuario já cadastrado tente um nome ou senha diferente!')
        elif usuarioExistente == 0:
            try:
                with conexão.cursor() as cursor:
                    cursor.execute(f'insert into cadastros (nome, senha, nivel) values ("{nome}", "{senha}", 1)')
                    conexão.commit()   
                    print('\033[1;32mAutênticado!')        
            except:
                print('\033[1;31mErro ao inserir os dados no banco de dados!')
    return autenticado, usuarioMaster

def cadastrarProdutos():
    nome = input('Digite um nome do produto: ')
    ingredientes = input('Digite os ingredientes dos produtos: ')
    grupo = input('Digite o grupo pertecente a esse produto: ')
    preço = float(input('Digite o preço do produto: '))

    try:
        with conexão.cursor() as cursor:
            cursor.execute(f'insert into produtos (nome, ingredientes, grupo, preço) values ("{nome}", "{ingredientes}", "{grupo}", "{preço}")')
            conexão.commit()
            print('\033[1;32mProduto cadastrado com sucesso!')
    except:
        print('\033[1;31mErro ao cadastrar!')
while not autenticado:

    decisao = int(input('Digite 1 para logar e 2 para cadastrar: '))

    try:
        with conexão.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
            print(resultado)
    except:
        print('\033[1;31mErro ao conectar no banco de dados')
    
    autenticado, usuarioSupremo = logarCadastrar()
