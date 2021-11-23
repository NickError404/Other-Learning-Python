from tkinter import  *



janela = Tk()
janela.title('Curso Tkinter')
janela.geometry('300x300')

frame = Frame(janela, width=10, height=20, bg='cyan').grid(row=0, column=0)
Label(frame, text='teste do frame').grid(row=0, column=0)
janela.mainloop()
