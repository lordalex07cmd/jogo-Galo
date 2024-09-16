from tkinter import *

from time import sleep

janela = Tk()
global njogadas


njogadas = 0


def relogio(minuto, segundo): 
    print(minuto, segundo)
    tempo = minuto*60 + segundo
    #Formatações
    if 5 < tempo < 10:
        lrelogio["fg"]="#FFA07A"
    elif tempo < 6:
        lrelogio["fg"]="#FF0000"
        
    if tempo == 0:
        lfim["text"]="FIM DO JOGO"
 #ATUALIZAÇÃO DE TEMPO
    if tempo > -1:
        lrelogio["text"]=f"00:{minuto}:{segundo}"
        if (segundo==0 and minuto != 0):
            minuto -=1
            segundo = 59
        #elif (segundo==0 and minuto == 0):
        #    segundo = 59
        else:
            segundo -=1
            
        lrelogio.after(1000, lambda: relogio(minuto, segundo))  

def escolheimg():
    if njogadas %2 == 1:
        return galo1
    return galo2



def new_game():
    b1.configure(state=NORMAL, text="", image="", width=6, height=3)
    b2.configure(state=NORMAL, text="", image="", width=6, height=3)
    b3.configure(state=NORMAL, text="", image="", width=6, height=3)
    b4.configure(state=NORMAL, text="", image="", width=6, height=3)
    b5.configure(state=NORMAL, text="", image="", width=6, height=3)
    b6.configure(state=NORMAL, text="", image="", width=6, height=3)
    b7.configure(state=NORMAL, text="", image="", width=6, height=3)
    b8.configure(state=NORMAL, text="", image="", width=6, height=3)
    b9.configure(state=NORMAL, text="", image="", width=6, height=3)

def verifica(jogador,posicao):
    if b1['text']==b2['text']==b3['text']!="":
        print("1")
        return jogador
    elif b4['text']==b5['text']==b6['text']!="":
        print("2")
        return jogador
    elif b7['text']==b8['text']==b9['text']!="":
        print("3")
        return jogador
    elif b1['text']==b4['text']==b7['text']!="":
        print("4")
        return jogador
    elif b2['text']==b5['text']==b8['text']!="":
        print("5")
        return jogador
    elif b3['text']==b6['text']==b9['text']!="":
        print("6")
        return jogador
    elif b1['text']==b5['text']==b9['text']!="":
        print("7")
        return jogador
    elif b3['text']==b5['text']==b7['text']!="":
        print("8")
        return jogador

    return -1

#confguracao dos botoes
def botao1():
    global njogadas
    njogadas +=1
    b1['width']=50
    b1['height']=50

    b1.configure(image=escolheimg())
    b1.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    print("RESP=",resp)
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao2():
    global njogadas
    njogadas +=1
    b2['width']=50
    b2['height']=50

    b2.configure(image=escolheimg())
    b2.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao3():
    global njogadas
    njogadas +=1
    b3['width']=50
    b3['height']=50

    b3.configure(image=escolheimg())
    b3.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao4():
    global njogadas
    njogadas +=1
    b4['width']=50
    b4['height']=50

    b4.configure(image=escolheimg())
    b4.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao5():
    global njogadas
    njogadas +=1
    b5['width']=50
    b5['height']=50

    b5.configure(image=escolheimg())
    b5.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao6():
    global njogadas
    njogadas +=1
    b6['width']=50
    b6['height']=50

    b6.configure(image=escolheimg())
    b6.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
   
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao7():
    global njogadas
    njogadas +=1
    b7['width']=50
    b7['height']=50

    b7.configure(image=escolheimg())
    b7.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)


def botao8():
    global njogadas
    njogadas +=1
    b8['width']=50
    b8['height']=50

    b8.configure(image=escolheimg())
    b8.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)

def botao9():
    global njogadas
    njogadas +=1
    b9['width']=50
    b9['height']=50

    b9.configure(image=escolheimg())
    b9.configure(state=DISABLED, text=njogadas%2)
    resp = verifica(njogadas%2, 1)
    
    if resp!=-1:
        print("vencedor foi jogador",resp)


def desiste():  
    print("Bebezinho!!")
    janela.destroy()





janela.title("Bem vindo ao Jogo do Galo")

tamx = 700 #tamanho da janela
tamy = 800
posx = 150 # posicao da janela no ecra
posy = 150


larg = int(janela.winfo_screenwidth()/2)
alt= int(janela.winfo_screenheight()/2)
janela.geometry (f"{tamx}x{tamy}+{posx}+{posy}")
janela.iconbitmap("galo1.ico")
janela.configure(bg="black")
janela.maxsize(width=900, height=400)
janela.minsize(width=250, height=380)

#radio button
v = StringVar(janela, "1")
values = {"Nivel iniciante" : "1",
          "Nivel Avançado" : "2",}

for (text, value) in values.items():

    Radiobutton(janela, text = text, variable = v,
                value = value, indicator = 0,
                background = "light pink").pack(fill = X, ipady = 5)

#imagens dos buttons
galo1 = PhotoImage(file="benfica.png")
galo2 = PhotoImage(file="sporting.png")



fonte = ("Comic Sans MS", 18,"italic", "bold")



f1 = Frame(janela)
f2 = Frame(janela)
f3 = Frame(janela)

texto1 = Label(f1,text="Campeonato Nacional",font=fonte).pack()

lrelogio = Label(janela, text="", font=fonte, fg="Blue")
lfim = Label(janela,text="", font=fonte, fg="Red")


b1 = Button(f2,width=6,height=3,command=botao1,text="")
b2 = Button(f2,width=6,height=3,command=botao2,text="")
b3 = Button(f2,width=6,height=3,command=botao3,text="")
b4 = Button(f2,width=6,height=3,command=botao4,text="")
b5 = Button(f2,width=6,height=3,command=botao5,text="")
b6 = Button(f2,width=6,height=3,command=botao6,text="")
b7 = Button(f2,width=6,height=3,command=botao7,text="")
b8 = Button(f2,width=6,height=3,command=botao8,text="")
b9 = Button(f2,width=6,height=3,command=botao9,text="")

cxtexto = Entry(janela, width=40, 
                bg="Gray",show="",
                font=fonte,
                fg="White")
cxtexto.focus()
botao = Button(janela, text="Desisto", command=desiste,bd=18,
               background="Lightgreen", foreground="Green")

novo = Button(janela,text="Novo Jogo",command=new_game,
              bg="yellow",fg="blue")




b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)


#Posicionar objetos
cxtexto.pack(side=BOTTOM)
botao.pack(side=LEFT, fill=BOTH)
novo.pack(side=RIGHT, fill=BOTH)

lrelogio.pack()
lfim.pack()
relogio(1,1)


f1.pack()
f2.pack()
f3.pack()



janela.mainloop()








    
    
    
