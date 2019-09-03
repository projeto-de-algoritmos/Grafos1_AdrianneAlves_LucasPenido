import pandas as pd
import json
from funcoesGrafo import *
from interface import *
from tkinter import *
from tkinter import font
from tkinter import ttk


def main():
    pd.read_csv('VoosAzul.csv').to_json('teste.json')

    with open('teste.json') as json_file:
        data = json.load(json_file)

    listaDeAdjacencia = {}
    listaAeroportos = []

    # Montando lista de adjacência
    for (key, aeroporto) in data['Aeroporto.Origem'].items():
        if not listaDeAdjacencia.get(aeroporto):
            listaDeAdjacencia[aeroporto] = []
            listaAeroportos.append(aeroporto)


        listaDeAdjacencia[aeroporto].append(data['Aeroporto.Destino'][key])

    listaAeroportos = sorted((set(listaAeroportos)))

    # Salvando lista de adjacência
    with open('listaAdkacência.json', 'w') as json_file:
        json.dump(listaDeAdjacencia, json_file)

    # print(listaDeAdjacencia)

    janelaPrincipal = Tk()
    janelaPrincipal.title("BUSCA-AZUL")
    janelaPrincipal.geometry("800x600+290+70") # width x height + x_offset + y_offset
    Application(janelaPrincipal, listaDeAdjacencia, data, listaAeroportos)

    janelaPrincipal.mainloop()

main()
