import requests
import pandas as pd

#senha para a api
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNTM1LCJpYXQiOjE3NTYzNzk1MzUsImp0aSI6ImIxZTZlODAzMTUxNjQzMDY5MjAwZTNhOWY2OGQwYTk0IiwidXNlcl9pZCI6IjgxIn0.nTf4k0ACnBVfgzaBEej4qrS-Oy-N5y_57C9KOF-SOnQ"
headers = {'Authorization': 'JWT {}'.format(token)}

for ticker in ["PETR4", "VALE3", "BBAS3"]:
    params = {
    'ticker': ticker,
    'ano_tri': '20252T',
    }

    response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
    response.status_code
    response = response.json()

    balanco = response["dados"][0]["balanco"]

    df = pd.DataFrame(balanco)

    filtro = (
        (df["conta"]=="3.11") &
        (df["descricao"].str.contains("^lucro", case = False)) &
        (df["data_ini"]=="2025-01-01")
        )

    lucro_liquido = df.loc[filtro, ["valor"]].iloc[0]

    filtro = (
        (df["conta"].str.contains("2.0.", case = False)) & 
        (df["descricao"].str.contains("^patrim", case = False))
        )

    pl = df.loc[filtro, ["valor"]].iloc[0]
    roe = lucro_liquido/pl
    print("ROE da", ticker, "é igual a:", roe)

