from tkinter import *
def clique():
     texto.configure(text="Botão Clicado!!!")
tela = Tk()

tela.geometry("200x100")
texto = Label(tela, text="Clique aqui")
texto.pack()

botao = Button(tela, text="Clique", command="")
botao.pack()

tela.mainloop()