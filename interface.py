from tkinter import *
from tkinter import font
from tkinter import ttk
from funcoesGrafo import *
from autocomplete import AutocompleteEntry

class Application:
    def __init__(self, master=None, listaDeAdjacencia=dict, data=dict, lista=dict):
        self.fonte = font.Font(family="Times", size=12)
        self.master = master
        self.listaDeAdjacencia = listaDeAdjacencia
        self.data = data
        self.containerTitulo = Frame(master)
        self.containerTitulo["padx"] = 50
        self.containerTitulo["pady"] = 20
        self.containerTitulo.pack()
        self.titulo = Label(self.containerTitulo, text="Olá! Seja bem vindo ao Busca-Azul!")
        self.titulo["font"] = ("Times", "20", "bold")
        self.titulo.pack ()

        self.containerSubtitulo = Frame(master)
        self.containerSubtitulo["padx"] = 50
        self.containerSubtitulo["pady"] = 20
        self.containerSubtitulo.pack()
        self.titulo = Label(self.containerSubtitulo, text="Aqui você pode encontrar a menor rota que a Azul realiza\n para vôos nacionais")
        self.titulo["font"] = ("Times", "14")
        self.titulo.pack ()

        self.containerOrigem = Frame(master)
        self.containerOrigem["padx"] = 50
        self.containerOrigem["pady"] = 20
        self.containerOrigem.pack()
        self.lblAeroOrigem = Label(self.containerOrigem, text="Aeroporto Origem:", font=self.fonte, width=20)
        self.lblAeroOrigem.pack(side=LEFT)
        self.txtAeroOrigem = AutocompleteEntry(lista, self.containerOrigem)
        self.txtAeroOrigem["width"] = 80
        self.txtAeroOrigem["font"] = self.fonte
        self.txtAeroOrigem.pack()

        self.containerDestino = Frame(master)
        self.containerDestino["padx"] = 50
        self.containerDestino["pady"] = 20
        self.containerDestino.pack()
        self.lblAeroDestino = Label(self.containerDestino, text="Aeroporto Destino:", font=self.fonte, width=20)
        self.lblAeroDestino.pack(side=LEFT)
        self.txtAeroDestino = AutocompleteEntry(lista, self.containerDestino)
        self.txtAeroDestino["width"] = 80
        self.txtAeroDestino["font"] = self.fonte
        self.txtAeroDestino.pack()

        self.containerRetorno = Frame(master)
        self.containerRetorno["padx"] = 50
        self.containerRetorno["pady"] = 20
        self.containerRetorno.pack()
        self.lblAeroRetorno = Label(self.containerRetorno, text="Volta? (S|N)", font=self.fonte, width=20)
        self.lblAeroRetorno.pack(side=LEFT)
        self.txtAeroRetorno = Entry(master)
        self.txtAeroRetorno["width"] = 20
        self.txtAeroRetorno["font"] = self.fonte
        self.txtAeroRetorno.pack()

        self.ctBtnBuscar = Frame(master)
        self.ctBtnBuscar["padx"] = 20
        self.ctBtnBuscar["pady"] = 10
        self.ctBtnBuscar.pack()
        self.btnBuscar = Button(self.ctBtnBuscar, text="Encontrar", font=self.fonte, width=12)
        self.btnBuscar["command"] = self.imprimeInterfaceMenorCaminho
        self.btnBuscar.pack(side=LEFT)

        self.containerRota = Frame(master)
        self.containerRota["padx"] = 50
        self.containerRota["pady"] = 20
        self.containerRota.pack()

    def imprimeInterfaceMenorCaminho(self):
        labels = []
        origem = self.txtAeroOrigem.get()
        destino = self.txtAeroDestino.get()
        retorno = self.txtAeroRetorno.get()

        for label in self.containerRota.winfo_children():
            label.destroy()
        if(origem == '' or destino == '' or retorno == ''):
            self.lblTitulo = Label(self.containerRota, text="Todos os campos devem ser preenchidos! Por favor, digite novamente", font=self.fonte, width=70)
            self.lblTitulo.pack()
        elif(self.listaDeAdjacencia.get(origem) == None):
            self.lblTitulo = Label(self.containerRota, text="Não foi possível encontrar o aeroporto de origem", font=self.fonte, width=70)
            self.lblTitulo.pack()
        else:
            buscaIda = busca_largura(self.listaDeAdjacencia, origem, destino)
            if buscaIda == 0:
                self.lblTitulo = Label(self.containerRota, text="Não é possível chegar ao aeroporto de destino a partir do de origem", font=self.fonte, width=70)
                self.lblTitulo.pack()
            else:
                largura = buscaIda[0]
                nivel = buscaIda[1]
                pai = buscaIda[2]
                menor_caminho = constroi_menor_caminho(pai, origem, destino)

                self.lblTitulo = Label(self.containerRota, text="A menor rota seria passando pelos seguintes aeroportos:", font=self.fonte, width=70)
                self.lblTitulo.pack()
                for i in range(0, len(menor_caminho)):
                    variable = menor_caminho[i]
                    sample = Label(self.containerRota, text=variable, font=self.fonte)
                    labels.append(sample)
                    sample.pack()
            if retorno.upper() == 'S':
                grafo_inverso = inverte_grafo(self.listaDeAdjacencia)
                buscaVolta = busca_largura(grafo_inverso, origem , destino)
                if buscaVolta == 0:
                    self.lblTitulo = Label(self.containerRota, text="Não há passagem de volta", font=self.fonte, width=70)
                    self.lblTitulo.pack()
                else:
                    self.lblTitulo = Label(self.containerRota, text=" =====> Passagens de ida e volta emitidas", font=self.fonte, width=70)
                    self.lblTitulo.pack()

