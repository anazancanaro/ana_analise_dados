import requests
import pandas as pd

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNTM1LCJpYXQiOjE3NTYzNzk1MzUsImp0aSI6ImIxZTZlODAzMTUxNjQzMDY5MjAwZTNhOWY2OGQwYTk0IiwidXNlcl9pZCI6IjgxIn0.nTf4k0ACnBVfgzaBEej4qrS-Oy-N5y_57C9KOF-SOnQ"
headers = {'Authorization': 'JWT {}'.format(token)}

params = {
'data_base': '2025-09-01'
}

response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)

response = response.json()
dados = response ["dados"]
df = pd.DataFrame(dados)

filtro = df["setor"] =="construção"
tickers = df.loc[filtro, "ticker"].values
lista_resultados = []

#início do for loop
for ticker in tickers:
    params = {
        'ticker':ticker,
        'ano_tri':'20252T',
    }
    response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
    response.status_code
    response = response.json()
    dados = response["dados"][0]
    balanco = dados["balanco"]
    df = pd.DataFrame(balanco)
    #Lucro líquido
    filtro = (
        (df["conta"]=="3.11") &
        (df["descricao"].str.contains("^lucro", case=False)) &
         (df["data_ini"]=="2025-01-01")
        )

    lucro_liquido = df.loc[filtro, ["valor"]].iloc[0]

    filtro = (
        (df["conta"].str.contains("2.0.", case = False)) & 
        (df["descricao"].str.contains("^patrim", case = False))
        )

    pl = df.loc[filtro, ["valor"]].iloc[0]
    roe = lucro_liquido/pl
    roe = roe.iloc[0]
    resultados = {
        "ticker":ticker,
        "roe":roe
    }
    lista_resultados.append(resultados)
    print(ticker,roe)
df_final = pd.DataFrame(lista_resultados)

df_maior = df_final.sort_values(by = "roe", ascending = False)


#Planilhao
import requests
import pandas as pd
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'data_base': '2025-09-01'}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
response = response.json()
dados = response["dados"]
df = pd.DataFrame(dados)
filtro = df["setor"]=="construção"
tickers = df.loc[filtro, "ticker"].values
lista_resultado1 = []
# Inicio do for loop
for ticker in tickers:
    params = {
        'ticker': ticker,
        'ano_tri': '20252T',
        }
    response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
    response.status_code
    response = response.json()
    dados = response["dados"][0]
    balanco = dados["balanco"]
    df = pd.DataFrame(balanco)
    # Lucro Liquido
    filtro = (
            (df["conta"]=="3.11") &
            (df["descricao"].str.contains("^lucro", case=False)) &
            (df["data_ini"]=="2025-01-01")
            )
    lucro_liquido = df.loc[filtro, ["valor"]].iloc[0]
    # PL
    filtro = (
            (df["conta"].str.contains("2.0.", case=False)) &
            (df["descricao"].str.contains("^patrim", case=False))
            )
    pl = df.loc[filtro, ["valor"]].iloc[0]
    roe = lucro_liquido / pl
    roe = roe.iloc[0]
    resultados = {
                "ticker":ticker,
                "roe": roe
        }
    lista_resultado1.append(resultados)
    print(ticker, roe)
df_1 = pd.DataFrame(lista_resultado1)
df_1.sort_values(["roe"])

#--------------------------------EXERCÍCIO PARA CASA--------------------------------------
#ROIC
import requests
import pandas as pd
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNTM1LCJpYXQiOjE3NTYzNzk1MzUsImp0aSI6ImIxZTZlODAzMTUxNjQzMDY5MjAwZTNhOWY2OGQwYTk0IiwidXNlcl9pZCI6IjgxIn0.nTf4k0ACnBVfgzaBEej4qrS-Oy-N5y_57C9KOF-SOnQ"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'data_base': '2025-09-01'}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
response = response.json()
dados = response["dados"]
df = pd.DataFrame(dados)
filtro = df["setor"]=="construção"
tickers = df.loc[filtro, "ticker"].values
lista_resultado2 = []
# Inicio do for loop
for ticker in tickers:
    params = {
        'ticker': ticker,
        'ano_tri': '20252T',
        }
    response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
    response.status_code
    response = response.json()
    dados = response["dados"][0]
    balanco = dados["balanco"]
    df = pd.DataFrame(balanco)
    # Lucro Operacional
    filtro = (
            (df["conta"].str.contains("3.05", case=False)) &
            (df["descricao"].str.contains("^resultado antes", case=False)) &
            (df["data_ini"]=="2025-01-01")
            )
    ebit = df.loc[filtro, ["valor"]].iloc[0]
    # PL
    filtro = (
            (df["conta"].str.contains("2.0.", case=False)) &
            (df["descricao"].str.contains("^patrim", case=False))
            )
    pl = df.loc[filtro, ["valor"]].iloc[0]
    # Emprestimos
    filtro = (
            (df["conta"].str.contains("2.01.04", case= False)) &
            (df["descricao"].str.contains("^empr.stimos.*", case=False))
            )
    emprestimos = df.loc[filtro, ["valor"]].iloc[0]
    roic = ebit / (pl+emprestimos)
    roic = roic.iloc[0]
    resultados = {
                "ticker":ticker,
                "roic": roic
        }
    lista_resultado2.append(resultados)
    print(ticker, roic)
df_2 = pd.DataFrame(lista_resultado2)
df_2.sort_values(["roic"])

df_final = pd.merge(df_1,df_2)
print(df_final)

df_final["media"] = (df_final["roic"]+df_final["roe"])/2
df_final.sort_values(["media"], ascending =False)