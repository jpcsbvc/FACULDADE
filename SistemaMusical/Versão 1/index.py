from tkinter import *
from tkinter.ttk import Combobox

lista_albuns = []

def envio ():
    nome_album = txtfld_nome_album.get()
    nome_artista = txtfld_nome_artista.get()
    data_lancamento = txtfld_data_lancamento.get()
    foi_lancamento = "Sim" if v0.get() == 1 else "Não"
    
    album = {
        "Nome do Álbum": nome_album,
        "Data de Lançamento": data_lancamento,
        "Artista ou Grupo Musical": nome_artista,
        "Foi Álbum de Lançamento": foi_lancamento
    }

    lista_albuns.append(album)

    txtfld_nome_album.delete(0, END)
    txtfld_data_lancamento.delete(0, END)
    txtfld_nome_artista.delete(0, END)
    v0.set(1)

    exibir_dados()

def exibir_dados():
    text_box.delete(1.0, END)

    for album in lista_albuns:
        text_box.insert(END, f"Nome do Álbum: {album['Nome do Álbum']}\n")
        text_box.insert(END, f"Data de Lançamento: {album['Data de Lançamento']}\n")
        text_box.insert(END, f"Artista ou Grupo Musical: {album['Artista ou Grupo Musical']}\n")
        text_box.insert(END, f"Foi Álbum de Lançamento: {album['Foi Álbum de Lançamento']}\n")
        text_box.insert(END, "\n")


window = Tk()
window.title("MusicINFO")
window.geometry('600x600')
lbl = Label(window, text="Bem vindo ao MusicINFO", fg='red', font=("Helvetica"))
lbl.pack()

lbl = Label(window, text="Ajude-nos a cadastrar alguns dados sobre álbuns históricos da música.")
lbl.pack()

lbl= Label(window, text="Insira o nome do album:")
lbl.pack()
txtfld_nome_album=Entry(window, bd=0)
txtfld_nome_album.pack() 
lbl= Label(window, text="Insira a data de lançamento:") 
lbl.pack()
txtfld_data_lancamento=Entry(window, bd=0)
txtfld_data_lancamento.pack() 
lbl= Label(window, text="Insira o nome do artista ou grupo musical:") 
lbl.pack()
txtfld_nome_artista=Entry(window, bd=0)
txtfld_nome_artista.pack() 
lbl= Label(window, text="Foi álbum de lançamento?") 
lbl.pack()
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="Sim", variable=v0, value=1)
r2= Radiobutton(window, text="Não", variable=v0, value=2)
r1.pack()
r2.pack()
btn = Button(window, text="Confirmar envio", command=envio)
btn.pack()

text_box = Text(window, height=10, width=50)
text_box.pack()

window.mainloop()



