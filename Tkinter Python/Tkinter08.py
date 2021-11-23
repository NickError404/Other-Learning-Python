from tkinter import  *
import pymysql
from tkinter import messagebox
from tkinter import  ttk

class AdminJanela():

    def CadastrarProduto(self):
        self.cadastrar = Toplevel()
        self.cadastrar.title('Cadastro de Produtos')
        self.cadastrar['bg'] = '#524f4f'

        Label(self.cadastrar, text='Cadastre os Produtos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4, pady=5, padx=5)

        Label(self.cadastrar, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.ingredientes = Entry(self.cadastrar)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.cadastrar)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Preço', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.preco = Entry(self.cadastrar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)


        Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.CadastrarProdutoBackEnd).grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.RemoverCadastrosBackEnd).grid(row=5, column=1, padx=5, pady=5) 
        Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.MostrarProdutosBackEnd).grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar Produtos', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.LimparCadastrosBackEnd).grid(row=6, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')
        
        self.tree.column("column1", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=400, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column("column3", width=400, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column("column4", width=60, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')


        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)
        

        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()

    def MostrarProdutosBackEnd(self):

        try:
            conexao = pymysql.connect(

            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        )

        except:
            print('\033[1;31mErro ao conectar ao banco de dados!')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultados = cursor.fetchall()
        except:
            print('\033[1;31mErro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []
    
        for linha in resultados:
            linhav.append(linha['nome'])
            linhav.append(linha['ingredientes'])
            linhav.append(linha['grupo'])
            linhav.append(linha['preco'])

            self.tree.insert("", END, values=linhav, iid=linha['id'], tag=1)

            linhav.clear()

    def CadastrarProdutoBackEnd(self):

        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'insert into produtos(nome, ingredientes, grupo, preco) values ("{nome}", "{ingredientes}", "{grupo}", "{preco}")')
                conexao.commit()
        except:
            print('Erro ao fazer consulta')
        self.MostrarProdutosBackEnd()

    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN')
        
        Button(self.root, text='Pedidos', width=20, bg='#E9C425', command=self.Pedidos).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Cadastros', width=20, bg='#F1B62D', command=self.CadastrarProduto).grid(row=1, column=0, padx=10, pady=10)

        self.root.mainloop()

    def RemoverCadastrosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(

            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        )

        except:
            print('\033[1;31mErro ao conectar ao banco de dados!')

        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'delete from produtos where id = {idDeletar}')
                conexao.commit()
        except:
            print('\033[1;31mErro ao fazer a consulta')
        self.MostrarProdutosBackEnd()

    def LimparCadastrosBackEnd(self):
        if messagebox.askokcancel('Limpar dados Cuidado!', 'DESEJA EXCLUIR TODOS OS DADOS DA TABELA? HÁ VOLTA'):
            try:
                conexao = pymysql.connect(

                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor

            )

            except:
                print('\033[1;31mErro ao conectar ao banco de dados!')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f'truncate table produtos;')
                    conexao.commit()
            except:
                print('\033[1;31mErro ao fazer a consulta')
            
            self.MostrarProdutosBackEnd()
    
    def Pedidos(self):

        self.pd = Toplevel()
        self.pd.resizable(False, False)
        self.pd.title('Realizar Pedidos')
        self.pd['bg'] = '#524f4f'

        Label(self.pd, text='Realizar Pedido', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4, pady=5, padx=5)

        Label(self.pd, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.pd)
        self.nome.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

        Label(self.pd, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, pady=5, padx=5)
        self.ingredientes = Entry(self.pd)
        self.ingredientes.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

        Label(self.pd, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, pady=5, padx=5)
        self.grupo = Entry(self.pd)
        self.grupo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
    
        Label(self.pd, text='Local de Entrega', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, pady=5, padx=5)
        self.LocalEntrega = Entry(self.pd)
        self.LocalEntrega.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        Label(self.pd, text='Observações', bg='#524f4f', fg='white').grid(row=5, column=0, columnspan=1, pady=5, padx=5)
        self.observacoes = Entry(self.pd)
        self.observacoes.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
        

        Button(self.pd, text='Cadastrar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.CadastrarPedidosbackEnd).grid(row=6, column=0, padx=5, pady=5)
        Button(self.pd, text='Excluir', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.RemoverPedidosBackEnd).grid(row=6, column=1, padx=5, pady=5)
        Button(self.pd, text='Atualizar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.VerPedidosBackEnd).grid(row=7, column=0, padx=5, pady=5)
        Button(self.pd, text='Limpar Produtos', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.LimparCadastrosBackEnd).grid(row=7, column=1, padx=5, pady=5)
        Button(self.pd, text='Visualizar Pedidos', width=30, bg='#F6FF2E', relief='flat', highlightbackground='#524f4f', command=self.visualTrue).grid(row=8, column=0, columnspan=4, padx=5, pady=5)

    
        self.pd.mainloop()

    def visualTrue(self):
            self.tree = ttk.Treeview(self.pd, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        
            self.tree.column("column1", width=150, minwidth=500, stretch=NO)
            self.tree.heading('#1', text='Nome')

            self.tree.column("column2", width=250, minwidth=500, stretch=NO)
            self.tree.heading('#2', text='Ingredientes')

            self.tree.column("column3", width=150, minwidth=500, stretch=NO)
            self.tree.heading('#3', text='Grupo')

            self.tree.column("column4", width=150, minwidth=500, stretch=NO)
            self.tree.heading('#4', text='Local de Entrega')

            self.tree.column("column5", width=250, minwidth=500, stretch=NO)
            self.tree.heading('#5', text='Observaçoes')

            self.tree.grid(row=0, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

            self.VerPedidosBackEnd()

    def CadastrarPedidosbackEnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        localEntrega = self.LocalEntrega.get()
        observacoes = self.observacoes.get()

        try:
            conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'insert into pedidos(nome, ingredientes, grupo, localEntrega, observacoes) values ("{nome}", "{ingredientes}", "{grupo}", "{localEntrega}", "{observacoes}")')
                conexao.commit()
        except:
            print('Erro ao fazer consulta')
        
        self.VerPedidosBackEnd()

    def VerPedidosBackEnd(self):

        try:
            conexao = pymysql.connect(

            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        )

        except:
            print('\033[1;31mErro ao conectar ao banco de dados!')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                resultados = cursor.fetchall()
        except:
            print('\033[1;31mErro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []
    
        for linha in resultados:
            linhav.append(linha['nome'])
            linhav.append(linha['ingredientes'])
            linhav.append(linha['grupo'])
            linhav.append(linha['localEntrega'])
            linhav.append(linha['observacoes'])

            self.tree.insert("", END, values=linhav, iid=linha['id'], tag=1)

            linhav.clear()

    def RemoverPedidosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(

            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        )

        except:
            print('\033[1;31mErro ao conectar ao banco de dados!')

        try:
            with conexao.cursor() as cursor:
                cursor.execute(f'delete from pedidos where id = {idDeletar}')
                conexao.commit()
        except:
            print('\033[1;31mErro ao fazer a consulta')
        self.VerPedidosBackEnd()

    def LimparPedidosBackEnd(self):
        if messagebox.askokcancel('Limpar dados Cuidado!', 'DESEJA EXCLUIR TODOS OS DADOS DA TABELA? HÁ VOLTA'):
            try:
                conexao = pymysql.connect(

                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor

            )

            except:
                print('\033[1;31mErro ao conectar ao banco de dados!')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f'truncate table pedidos;')
                    conexao.commit()
            except:
                print('\033[1;31mErro ao fazer a consulta')
            
            self.VerPedidosBackEnd()

class JanelaLogin():

    def VerificaLogin(self):

        autenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(

            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        )

        except:
            print('\033[1;31mErro ao conectar ao banco de dados!')

        usuario = self.email.get()
        senha = self.senha.get()
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('\033[1;31mErro ao fazer a consulta')

        for linha in resultados:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        
        if not autenticado:
            messagebox.showinfo('Login erro', 'Email ou Senha inválido!')

        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                AdminJanela()

    def CadastroBackEnd(self):
        codigoPadrao = '123@h'
        if self.codigoSegurança.get() == codigoPadrao:
            if len(self.email.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.email.get()
                    senha = self.senha.get()

                    try:
                        conexao = pymysql.connect(

                        host='localhost',
                        user='root',
                        password='',
                        db='erp',
                        charset='utf8mb4',
                        cursorclass = pymysql.cursors.DictCursor

                    )

                    except:
                        print('\033[1;31mErro ao conectar ao banco de dados!')

                    with conexao.cursor() as cursor:
                        cursor.execute(f'insert into cadastros (nome, senha, nivel) values ("{nome}","{senha}", 1)')
                        conexao.commit()
                    messagebox.showinfo('Cadastro', 'usuario cadastrado com sucesso')
                    self.root.destroy()
                else:
                    messagebox.showerror('Senha Inválida', 'Por favor coloque uma senha no máximo com 50 caracteres')
            else:
                messagebox.showerror('Nome inválido', 'Por vaor inserir um nome no máximo com 20 caracteres')
        else:
            messagebox.showerror('Código de vericação inválido', 'Código digitado incorretamente')

    def Cadastro(self):

        Label(self.root, text='Chave de segurança').grid(row=3, column=0, pady=5, padx=5)
        self.codigoSegurança = Entry(self.root, show='*')
        self.codigoSegurança.grid(row=3, column=1, pady=5, padx=10)
        Button(self.root, text='Confirmar cadastro', width=15, bg='blue1', command=self.CadastroBackEnd).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

    def UpdateBackEnd(self):
        
        try:
            conexao = pymysql.connect(

            host='localhost',
            user='root',
            password='',
            db='erp',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        )

        except:
            print('\033[1;31mErro ao conectar ao banco de dados!')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('\033[1;31mErro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []

        for linha in resultados:
            linhav.append(linha['id'])
            linhav.append(linha['nome'])
            linhav.append(linha['senha'])
            linhav.append(linha['nivel'])

            self.tree.insert("", END, values=linhav, iid=linha['id'], tag=1)

            linhav.clear()

    def visualizarCadastros(self):

        self.vc = Toplevel()
        self.vc.resizable(False, False)
        self.vc.title('Visualizar cadastros')

        self.tree = ttk.Treeview(self.vc, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')
        
        self.tree.column("column1", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Usuario')

        self.tree.column("column3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column("column4", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Nivel')


        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.UpdateBackEnd()

        self.vc.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')

        Label(self.root, text='Faça seu login', fg='black').grid(row=0, column=0, columnspan=2)
        Label(self.root, text='Digite seu email').grid(row=1, column=0)
        
        self.email = Entry(self.root)
        self.email.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text='Digite sua senha').grid(row=2, column=0)

        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='Login', bg='green3', width=10, command=self.VerificaLogin).grid(row=5, column=0, padx=5, pady=5)
        
        Button(self.root, text='Cadastrar', bg='orange3', width=10, command=self.Cadastro).grid(row=5, column=1, padx=5, pady=5)

        Button(self.root, text='Visualizar cadastros', bg='white', command=self.visualizarCadastros).grid(row=6, column=0, columnspan=2, padx=5, pady=5)


        self.root.mainloop()

JanelaLogin()
