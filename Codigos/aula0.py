#REVISÃO BÁSICA DE PYTHON

#faz um input
x = float(input())

#faz uma condicional da nota
if x > 7:
    print("Você passou!")
else:
    print("Você é burro")

#definir variaveis
x = "lucro"
y = 1345980.19
z = 4

#lista e dicionário
lista = [x,y,z]

dicionario = {"Objetivo": x,
              "Total": y,
              "Culturas": z}


#importar a biblioteca pandas pra ler o arquivo
import pandas as pd

#salva numa variável
df = pd.read_excel("C:/Users/ana/OneDrive/Área de Trabalho/IBMEC/Semestre_4/Analise_Dados/Arquivos/livros_classics.xlsx")


