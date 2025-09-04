import requests as rq
import pandas as pd

cep = "71660730"
url = f"https://viacep.com.br/ws/{cep}/json/"

response =  rq.get(url)
response.json()

#importar os dados da api do ipea
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"

response = rq.get(url)
metadados = response.json()

#transforma em dataframe pra ficar mais visual
df = pd.DataFrame(metadados)

#acessar o codigo do IBGE
SERCODIGO = "HOMIC"
url =  f"http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{SERCODIGO}')"
response = rq.get(url)

dados = response.json()
dados = dados["value"]

df = pd.DataFrame(dados)
df.shape
df.columns
df.info()
filtro_brasil = df["NIVNOME"]=="Brasil"
df_brasil = df.loc[filtro_brasil]
df_brasil[["VALDATA", "VALVALOR"]].plot()

df_brasil["VALDATA"].dt.year