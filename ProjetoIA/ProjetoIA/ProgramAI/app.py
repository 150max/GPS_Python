import cidade
from queue import PriorityQueue
from tkinter import *

root = Tk()
root.configure(bg="#90dea4")
root.title("Metodos de Procura")

#90dea4recuperar os dados da class
mapa = cidade.Cidade()

#90dea4recuperar os dados de cada grafo
cidadesLigadas = mapa.CidadesVizinhas()
cidadeReta = mapa.LinhaReta()
cidadeRetaFaro  = mapa.DistanciaReta()
pesos = mapa.Peso()
#90dea4#90dea4
label1 = Label(text="MÉTODOS DE PROCURA")
label1.configure(bg="#90dea4")
label1.pack(pady=(10,20))


def profundidade_limitada(inicio, fim, caminho, iteracao, limite, is_first):
    if is_first==True:
        print("\n**********Profundidade Limitada**********")
        caminho.clear()
    else:
        pass
    print('\nIteração-->', iteracao)
    print('A testar', inicio)
    caminho.append(inicio)
    if inicio == fim:
        print('Chegou ao destino')
        print('Caminho: ',caminho)
        return caminho
    print('Não é o nó final')
    if iteracao == limite:        
        return False
    print('\nExpandindo o nó atual', inicio)
    for no in cidadesLigadas[inicio]:
        if profundidade_limitada(no, fim, caminho, iteracao+1, limite, is_first=False):
            return caminho            
        caminho.pop()
    print('\nNão consegue chegar ao destino com esse limite, defina um novo')
    return False
    


def return_peso(no_inicio, no_para, tamanho):
    return tamanho.get((no_inicio, no_para)) if tamanho else 1
    
def custo_uniforme(graph, inicio, fim, peso):

    print("\n**********Custo Uniforme**********\n")
    fronteira = PriorityQueue()
    fronteira.put((0,inicio))
    print('Iteração 0')
    print(inicio)
    pos = 1
    while True:
        ucs_w, no_atual = fronteira.get()

        if no_atual == fim:
            print('-'*100)
            print('No escolhido ' + fim)
            print('FIM')
            return
        print('-'*100)
        print('Iteração '+str(pos))
        for no in graph[no_atual]:
            fronteira.put((ucs_w + return_peso(no_atual, no, peso), no))
        print(sorted(fronteira.queue))
        if fronteira.queue[0][1] is not fim:
            print('Para abrir ---> ' + str(fronteira.queue[0][1] + '.'))
        pos = pos+1

def sofrega(graph, inicio, fim,reta):

    print('\n**********Procura Sofrega**********\n')
    fronteira = PriorityQueue()
    fronteira.put((0,inicio))
    print('Iteração 0')
    print(inicio)
    pos = 1
    valor = False
    while True:
            
        ucs_w, no_atual = fronteira.get()
        if valor:
            ucs_w = return_peso(no_atual, fim, reta)

        if no_atual == fim:
            print('-'*100)
            print('No escolhido ' + fim)
            print('FIM')
            return

        print('-'*100)
        print('Iteração '+str(pos))
        for no in graph[no_atual]:
            fronteira.put((return_peso(no, fim, reta), no))
        print(sorted(fronteira.queue))
        if fronteira.queue[0][1] is not fim:
            print('Para abrir ---> ' + str(fronteira.queue[0][1] + '.'))
        pos = pos+1
        valor = True

def a_estrela(graph, inicio, fim, peso, reta):
    print('\n********** A* **********\n')
    fronteira = PriorityQueue()
    fronteira.put((0,inicio))
    print('Iteração 0')
    print(inicio)
    pos = 1
    valor = False
    while True:
        
        ucs_w, no_atual = fronteira.get()
        if valor:
            ucs_w = ucs_w - return_peso(no_atual, fim, reta)

        if no_atual == fim:
            print('-'*100)
            print('No escolhido ' + fim)
            print('FIM')
            return
        
        print('-'*100)
        print('Iteração '+str(pos))
        for no in graph[no_atual]:
            fronteira.put((ucs_w + return_peso(no_atual, no, peso)+return_peso(no, fim, reta), no))
        print(sorted(fronteira.queue))
        if fronteira.queue[0][1] is not fim:
            print('Para abrir ---> ' + str(fronteira.queue[0][1] + '.'))
        pos = pos+1
        valor = True

var1 = StringVar()
var2 = StringVar()
var3 = IntVar()
    
welcome ="Bem vindo aos métodos de procura."
labelwelcome = Label(root, text=welcome)
labelwelcome.configure(bg="#90dea4")
labelwelcome.pack(pady=(5,10))

label2 = Label(text="Origem")
label2.configure(bg="#90dea4")
label2.pack(pady=(2,0))
e1 = Entry(textvariable=var1, width=40)
e1.pack(ipady=5, pady=(10,0), padx=(20,20))
    
label3 = Label(text="Destino")
label3.configure(bg="#90dea4")
label3.pack(pady=(2,0))
e2 = Entry(textvariable=var2, width=40)
e2.pack(ipady=5,pady=5, padx=(20,20))
    
label4 = Label(text="Limite (Profundidade Limitada)")
label4.configure(bg="#90dea4")
label4.pack(pady=(2,0))
e3 = Entry(textvariable=var3, width=40)
e3.pack(ipady=5,pady=5, padx=(20,20))
  
a_fim_faro = "Faro"
path = list()
    
button1 = Button(root, text="Profundidade Limitada", command=lambda:profundidade_limitada(var1.get(), var2.get(),path, 0, var3.get(), True), height=1, width=35)
button1.pack(pady=(10,0), padx=(30,30)) 
button2 = Button(root, text="Custo Uniforme", command=lambda:custo_uniforme(cidadeReta, var1.get(), var2.get(), pesos), height=1, width=35)
button2.pack(pady=(10,0), padx=(30,30))
button3 = Button(root, text="Sôfrega", command=lambda:sofrega(cidadeReta, var1.get(), a_fim_faro,cidadeRetaFaro), height=1, width=35)
button3.pack(pady=(10,0), padx=(30,30))
button4 = Button(root, text="A Estrela (A*)", command=lambda:a_estrela(cidadesLigadas, var1.get(), a_fim_faro, pesos,cidadeRetaFaro), height=1, width=35)
button4.pack(pady=(10,15), padx=(30,30))
button5 = Button(root, text="Sair", command=lambda:root.destroy(), height=1, width=25)
button5.pack(pady=(15,15), padx=(50,50))

imagem = PhotoImage(file="Mapa_Portugal1.png")
w = Label(root, image=imagem)
w.imagem = imagem
w.pack(pady=(0,15))

def init():
    labelwelcome.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()   
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    
def methods(name):
    init()
        
root.mainloop()