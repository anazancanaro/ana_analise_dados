import pandas as pd

#salva num data frame
df = pd.read_excel("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\cadastro_alunos.xlsx")

#observa os dados no df
df.columns
df.head()

#usa os caracteres (^ . | $) do regex pra filtrar de forma rápida e fácil
filtro = df["nome_aluno"].str.contains("^maria|^ana|^isabela", case=False)
df.loc[filtro]

import requests as rq
import json

#importar os dados da api do ipea
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"

response = rq.get(url)
metadados = response.json()

metadados = metadados["value"]

#transforma em dataframe pra ficar mais visual
data = pd.DataFrame(metadados)

data.columns

data.head()

filtro2 = data["SERNOME"].str.contains("IPCA - educação, leitura e papelaria - taxa de variação", case=False)
data.loc[filtro2, "SERNOME"].values
data.loc[filtro2]

url =  "http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='PRECOS12_IPCAED12')"
response = rq.get(url)

dados = response.json()
dados = dados["value"]

df = pd.DataFrame(dados)

df["VALDATA"] = pd.to_datetime(df["VALDATA"], errors = "coerce")
df[["VALDATA", "VALVALOR"]].plot() 

#outra api

uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'd7faf6befd2f49bbba7bdd9f29bae187' }

response = rq.get(uri, headers=headers)
data = response.json()
data = data["matches"]
df = pd.DataFrame(data)

df.head()