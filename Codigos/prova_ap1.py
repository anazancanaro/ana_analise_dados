# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), 
# que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv e ncr_ride_regions.xlsx para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

import pandas as pd

# 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
dados = pd.read_csv("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\ncr_ride_bookings.csv")
df = pd.DataFrame(dados)

df.columns

df_completo = df["Booking Status"]=="Completed"

df_completo.value_counts() # deram 93000 corridas completas


# 2 - Qual a proporção em relação ao total de corridas?

filtro = (df["Booking Status"]=="Completed")
df1 = df.loc[filtro]

proporcao = len(df1)/len(df) #proporção de 62%

# 3 - Calcule a média e mediana da Distância percorrida por cada Tipo de veículo.

media = df.groupby("Vehicle Type")["Ride Distance"].mean()
mediana = df.groupby("Vehicle Type")["Ride Distance"].median()

# 4 - Qual o Metodo de Pagamento mais utilizado pelas bicicletas ("Bike") ?

filtro = df["Vehicle Type"] == "Bike"
df = df.loc[filtro]
df.value_counts("Payment Method") #método UPI é o mais comum

# 5 - Faca um merge com ncr_ride_regions.xlsx pela coluna ("Pickup Location") para pegar as regioes das corridas.
# e verifique qual a Regiao com o maior Valor da corrida?

regioes = pd.read_excel("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\ncr_ride_regioes.xlsx")
df2 = pd.DataFrame(regioes)
df = pd.DataFrame(dados)

df_final = pd.merge(df, df2, on = "Pickup Location", how = "inner")

maior = df_final["Booking Value"].max()
filtro = df_final["Booking Value"] == maior
regiao_maior = df_final.loc[filtro, "Regiao"].iloc[0] #regiao Norte possui a corrida mais cara


# 6 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados"
# e filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“venda”).
# Dica Técnica, filtre atraves das coluna FNTSIGLA: df["FNTSIGLA"].str.contains() 
# e depois SERNOME: df["SERNOME"].str.contains() 

import requests

api = "http://www.ipeadata.gov.br/api/odata4/Metadados"
dados = requests.get(api).json()["value"]
df = pd.DataFrame(dados)

df_fipe = df[df["FNTSIGLA"].str.contains("Fipe", case=False)]
df_fipe[df_fipe["SERNOME"].str.contains("venda", regex=True, case=False)]



# Descubra qual é o código da série correspondente.
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# e construa um DataFrame pandas com as datas (DATA) e os valores (VALVALOR).
# Converta a coluna de datas para o formato adequado (pd.to_datetime())

# 7 -  Monte um gráfico de linha mostrando a evolução das vendas ao longo do tempo.
# Dica: você pode usar a biblioteca matplotlib para gerar o gráfico.


CODIGO_ENCONTRADO = 'FIPE12_VENBR12'
api =  f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
dados = requests.get(api).json()["value"]
df = pd.DataFrame(dados)

df = df[["VALDATA", "VALVALOR"]]
df["VALDATA"]=pd.to_datetime(df["VALDATA"], utc=True, errors="coerce")
df["VALDATA"] = df["VALDATA"].dt.tz_convert("America/Sao_Paulo")
df["DATA"] = df["VALDATA"].dt.date

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(df["DATA"], df["VALVALOR"])
plt.title("Venda de Imóveis no Brasil, de 2008 a 2025")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.grid(True)
plt.show()


# 8 - Crie o grafico do bitcoin (ticker: "btc") atraves da api preco-diversos
# Pegue o periodo compreendido entre 2001 a 2025
# Monte um gráfico de linha mostrando a evolução do preco de fechamento
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3Nzk4LCJpYXQiOjE3NTg2MjU3OTgsImp0aSI6ImIyMWExM2RhMDQ5NjQxOGJhMmUyNzdhZjUwZDEwMWRjIiwidXNlcl9pZCI6IjkxIn0.i4sYfwHwCZBaA6yySFPjHw1gImPoTdcmKIzTq6U_4Gw"
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {
'ticker': 'btc',
'data_ini': '2001-01-01',
'data_fim': '2025-09-01'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/preco-diversos', params=params, headers=headers)
response = response.json()
dados = response["dados"]
df = pd.DataFrame(dados)

df["data"]=pd.to_datetime(df["data"], utc=True, errors="coerce")
df["data"] = df["data"].dt.tz_convert("America/Sao_Paulo")
df["data"] = df["data"].dt.date

plt.figure(figsize=(12,6))
plt.plot(df["data"], df["fechamento"])
plt.title("Preço de Fechamento do Bitcoin, de 2001 a 2025")
plt.xlabel("Ano")
plt.ylabel("Preço")
plt.grid(True)
plt.show()


# 9 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# A autenticação é feita via JWT Token no cabeçalho da requisição.
# Acesse a API no endpoint: https://laboratoriodefinancas.com/api/v1/planilhao
# passando como parâmetro a data (por exemplo, "2025-09-23").
# Construa um DataFrame pandas a partir dos dados recebidos.
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROC (Return on Capital) nessa data.
# Exiba o ticker da empresa, setor e o valor do ROC correspondente.
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3Nzk4LCJpYXQiOjE3NTg2MjU3OTgsImp0aSI6ImIyMWExM2RhMDQ5NjQxOGJhMmUyNzdhZjUwZDEwMWRjIiwidXNlcl9pZCI6IjkxIn0.i4sYfwHwCZBaA6yySFPjHw1gImPoTdcmKIzTq6U_4Gw"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {
'data_base': '2025-09-24'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
response = response.json()
dados = response["dados"]
df = pd.DataFrame(dados)

filtro = (df["setor"]=="tecnologia")
df = df.loc[filtro]
maior = df["roc"].max() 
filtro = df["roc"]==maior
tech_roc = df.loc[filtro].iloc[0]
tech_roc = tech_roc[["ticker","setor","roc"]] #CSUD3 é a que possui maior ROC


# 10 - A API do Laboratório de Finanças fornece informações de balanços patrimoniais de empresas listadas na B3.
# Acesse o endpoint: https://laboratoriodefinancas.com/api/v1/balanco
# usando a empresa Gerdau ("GGBR4") e o período 2025/2º trimestre (ano_tri = "20252T").
# O retorno da API contém uma chave "balanco", que é uma lista com diversas contas do balanço.
# Localize dentro dessa lista a conta cuja descrição é “Ativo Total” e "Lucro Liquido".
# Calcule o Return on Assets que é dados pela formula: ROA = Lucro Liquido / Ativo Totais

import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3Nzk4LCJpYXQiOjE3NTg2MjU3OTgsImp0aSI6ImIyMWExM2RhMDQ5NjQxOGJhMmUyNzdhZjUwZDEwMWRjIiwidXNlcl9pZCI6IjkxIn0.i4sYfwHwCZBaA6yySFPjHw1gImPoTdcmKIzTq6U_4Gw"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'ticker': 'GGBR4', 
          'ano_tri': '20252T'
          }
response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
response = response.json()
dados = response["dados"][0]
balanco = dados["balanco"]
df = pd.DataFrame(balanco)

df[df["descricao"].str.contains("^ativo total", regex=True, case=False)] #conta 1
df[df["descricao"].str.contains("^lucro l.quido", regex=True, case=False)] #conta 6.01.01.01

filtro = (
    (df["conta"]=="1") &
    (df["descricao"].str.contains("^ativo total", regex=True, case=False))
    )
ativo_total = df.loc[filtro, ["valor"]].iloc[0]

filtro = (
    (df["conta"]=="6.01.01.01") &
    (df["descricao"].str.contains("^lucro l.quido", regex = True, case=False))
    )

lucro_liquido = df.loc[filtro, ["valor"]].iloc[0]
roa = lucro_liquido / ativo_total