from tkinter import  *


janela = Tk()
janela.title('Curso de Python')
janela.geometry('500x500')
janela.resizable(False, False)

Label(janela, text='Olá Pessoal', bg='black', fg='orange3', padx=30, pady=30).grid(row=0, column=0)

janela.mainloop()
