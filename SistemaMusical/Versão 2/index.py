from tkinter import *
from tkinter.ttk import Combobox

var = 0

avenged_sevenfold = ["Sounding the Seventh Trumpet",  "Waking the Fallen", "City of Evil", "Avenged Sevenfold", "Nightmare", "Hail to the King", "The Stage", "Life Is But A Dream"]                     

black_sabbath = [ "Black Sabbath", "Paranoid", "Master of Reality", "Vol. 4", "Sabbath Bloody Sabbath", "Sabotage", "Technical Ecstasy", "Never Say Die!", "Heaven and Hell", "Mob Rules", "Born Again", "Seventh Star", "The Eternal Idol", "Headless Cross", "Tyr", "Dehumanizer", "Cross Purposes", "Forbidden", "13"]                      

iron_maiden = ["Iron Maiden", "Killers", "The Number of the Beast", "Piece of Mind", "Powerslave", "Somewhere in Time", "Seventh Son of a Seventh Son", "No Prayer for the Dying", "Fear of the Dark", "The X Factor", "Virtual XI", "Brave New World", "Dance of Death", "A Matter of Life and Death", "The Final Frontier",  "The Book of Souls", "Senjutsu"]

led_zeppelin = [ "Led Zeppelin", "Led Zeppelin II", "Led Zeppelin III", "Led Zeppelin IV", "Houses of the Holy", "Physical Graffiti", "Presence",  "In Through the Out Door", "Coda"]

metallica = ["Kill 'Em All", "Ride the Lightning", "Master of Puppets", "...And Justice for All", "Metallica (The Black Album)", "Load", "Reload", "St. Anger", "Death Magnetic", "Hardwired... to Self-Destruct", "72 seasons"]

pink_floyd = ["The Piper at the Gates of Dawn", "A Saucerful of Secrets", "More", "Ummagumma", "Atom Heart Mother", "Meddle", "Obscured by Clouds", "The Dark Side of the Moon", "Wish You Were Here", "Animals", "The Wall", "The Final Cut", "A Momentary Lapse of Reason", "The Division Bell", "The Endless River"]

artista_albums = {"Avenged Sevenfold" : avenged_sevenfold ,"Black Sabbath" : black_sabbath, "Iron Maiden" : iron_maiden, "Led Zeppelin" : led_zeppelin, "Metallica" : metallica, "Pink Floyd" : pink_floyd }

# separação

ano_albuns_avenged_sevenfold = {2001 : avenged_sevenfold[0], 2003 : avenged_sevenfold[1], 2005 : avenged_sevenfold[2] , 2007 : avenged_sevenfold[3], 2010 : avenged_sevenfold [4], 2013 : avenged_sevenfold[5], 2016 : avenged_sevenfold [6] , 2023 : avenged_sevenfold[7]}

ano_albuns_black_sabbath = {1970 : black_sabbath[0], 1970 : black_sabbath[1], 1971 : black_sabbath[2] , 1972 : black_sabbath[3], 1973 : black_sabbath [4], 1975 : black_sabbath[5], 1976 : black_sabbath [6] , 1978 : black_sabbath[7] , 1980 : black_sabbath[8] , 1981 : black_sabbath[9] , 1983 : black_sabbath[10] , 1986 : black_sabbath[11],  1987 : black_sabbath[12] , 1989 : black_sabbath[13] , 1990 : black_sabbath[14] , 1992 : black_sabbath[15] , 1994 : black_sabbath[16] , 1995 : black_sabbath[17],  2013 : black_sabbath[18]}

ano_albuns_iron_maiden = {1980 : iron_maiden[0], 1981 : iron_maiden[1], 1982 : iron_maiden[2] , 1983 : iron_maiden[3], 1984 : iron_maiden[4], 1986 : iron_maiden[5], 1988 : iron_maiden[6] , 1990 : iron_maiden[7] , 1992 : iron_maiden[8] , 1995 : iron_maiden[9] , 1998 : iron_maiden[10] , 2000 : iron_maiden[11],  2003 : iron_maiden[12] , 2006 : iron_maiden[13] , 2010 : iron_maiden[14] , 2015 : iron_maiden[15] , 2021 : iron_maiden[16]}

ano_albuns_led_zeppelin = {1969 : led_zeppelin[0], 1969 : led_zeppelin[1], 1970 : led_zeppelin[2] , 1971 : led_zeppelin[3], 1973 : led_zeppelin[4], 1975 : led_zeppelin[5], 1976 : led_zeppelin[6] , 1979 : led_zeppelin[7] , 1982 : led_zeppelin[8]}

ano_albuns_metallica = {1983 : metallica[0], 1984 : metallica[1], 1985 : metallica[2] , 1988 : metallica[3], 1991 : metallica[4], 1996 : metallica[5], 1997 : metallica[6] , 2003 : metallica[7] , 2008 : metallica[8], 2016 : metallica[9], 2023 : metallica[10]}

ano_albuns_pink_floyd = {1967 : pink_floyd[0], 1968 : pink_floyd[1], 1969 : pink_floyd[2] , 1969 : pink_floyd[3], 1970 : pink_floyd[4], 1971 : pink_floyd[5], 1972 : pink_floyd[6] , 1973 : pink_floyd[7] , 1975 : pink_floyd[8], 1977 : pink_floyd[9], 1979 : pink_floyd[10], 1983 : pink_floyd[11], 1987 : pink_floyd, 1994 : pink_floyd, 2014 : pink_floyd}

ano_albuns = {"Ano de album do Avenged Sevenfold " : ano_albuns_avenged_sevenfold, "Ano de album do Black Sabbath" : ano_albuns_black_sabbath, "Ano de album do Iron Maiden" : ano_albuns_iron_maiden, "Ano de album do Led Zeppelin" : ano_albuns_led_zeppelin, "Ano de album do Metallica" : ano_albuns_metallica, "Ano de album do Pink Floyd" : ano_albuns_pink_floyd}

def buscar():
    termo_busca = entry.get().upper()
    resultados = []

    for artista, albums in artista_albums.items():
        if termo_busca in artista.upper():
            resultados.append(f"Álbuns de {artista}: {', '.join(albums)}\n\n")

    if resultados:
        text_box.delete(1.0, END)  
        text_box.insert(END, "Resultados da busca:\n\n")
        text_box.insert(END, "\n".join(resultados))
    else:
        text_box.delete(1.0, END)
        text_box.insert(END, "Artista ou grupo musical não encontrado.\n\n")


def buscar_ano ():
    tempo_escolhido = var
    ano_escolhido = int(cb_ano.get())
    resultados_anos = []
    for anos_artistas in ano_albuns:
        for anos in ano_albuns[anos_artistas]:
            if tempo_escolhido == 0 and anos < ano_escolhido:                 
                resultados_anos.append(ano_albuns[anos_artistas][anos]) 
                text_box_ano_album.delete(1.0, END) 
                text_box_ano_album.insert(END,(resultados_anos), "\n\n") 
            elif tempo_escolhido == 1 and anos == ano_escolhido:
                resultados_anos.append(ano_albuns[anos_artistas][anos])
                text_box_ano_album.delete(1.0, END)
                text_box_ano_album.insert(END,(resultados_anos), "\n\n")
            elif tempo_escolhido == 2 and anos > ano_escolhido:
                resultados_anos.append(ano_albuns[anos_artistas][anos])
                text_box_ano_album.delete(1.0, END)
                text_box_ano_album.insert(END, (resultados_anos), "\n\n")
            # else:
                # text_box_ano_album.delete(1.0, END)
                # text_box_ano_album.insert(END, "Erro ou ano indisponível.")

def botao_selecionado (idx):
    var = idx

window = Tk()
window.title("MusicINFO")
window.geometry("600x600")

lbl = Label(window, text="Buscar álbuns por banda:")
lbl .pack()

lb = Listbox(window, selectmode="multiple")
for artista in artista_albums:
    lb.insert(END, artista)
lb.pack()

entry = Entry(window)
entry.pack()

btn = Button(window, text="Buscar", command=buscar)
btn.pack()

text_box = Text(window, height=10, width=50)
text_box.pack()

frame = Frame ()
frame.pack()

lbl_ano_album = Label(frame, text="Selecione um ano para visualizar os albuns lançados antes desse ano, no mesmo ano ou após esse ano, desses artistas.")
lbl_ano_album.pack()

cb_ano = Combobox(frame , values=list(range(1967,2024)))
cb_ano.pack()

radio_button_var = StringVar()

radio_button = Radiobutton(frame, text="Anterior a", variable=radio_button_var, value=0, command=lambda: botao_selecionado(0))
radio_button.pack()

radio_button = Radiobutton(frame, text="Igual", variable=radio_button_var, value=1, command=lambda: botao_selecionado(1))
radio_button.pack()

radio_button = Radiobutton(frame, text="Posterior", variable=radio_button_var, value=2 , command=lambda: botao_selecionado(2))
radio_button.pack()

btn_envio_ano = Button(window, text="Enviar" , command=buscar_ano)
btn_envio_ano.pack()

text_box_ano_album = Text(frame, height=10, width=100)
text_box_ano_album.pack()

window.mainloop()