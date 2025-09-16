import pandas as pd
df = pd.read_csv("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\imoveis_brasil.csv")

#QUESTÃO 1
df.head()
df.tail()
df.sample(5)

#QUESTÃO 2
df.shape

#QUESTÃO 3
df.columns

#QUESTÃO 4
df.dtypes

#QUESTÃO 5
df.describe()

#QUESTÃO 6
df.info()

#QUESTÃO 7
df['Tipo_Imovel'].unique()

#QUESTÃO 8
filtro = df["Valor_Imovel"]>= 1000000
df.loc[filtro]

#QUESTÃO 9
df2 = df[["Cidade","Bairro","Valor_Imovel"]]

#QUESTÃO 10
filtro = df["Cidade"]== "Curitiba"
df_curitiba = df.loc[filtro]

#QUESTÃO 11
df.isnull().sum()

#QUESTÃO 12
top_10 = df.sort_values(by="Valor_Imovel", ascending = False).head(10)

#QUESTÃO 13
media = df["Valor_Imovel"].mean()

#QUESTÃO 14
df["Valor_Imovel"].median()

#QUESTÃO 15
df["Valor_Imovel"].std()

#QUESTÃO 16
df["Valor_Imovel"].min()
df["Valor_Imovel"].max()

#QUESTÃO 17
maior = df["Valor_Imovel"] > media
maior.value_counts()

#QUESTÃO 18
df["valor_m2"] = df["Valor_Imovel"]/df["Area_m2"]

#QUESTÃO 19
df.loc[len(df)] = {
    'Cidade': 'Teste',
    'Valor_Imovel': 999999,
    'Area_m2': 100
}

#QUESTÃO 20
df.isnull().sum()

#QUESTÃO 21
df = df[df['Numero_Quartos'] != 5]

#QUESTÃO 22
df = df.drop(columns = ["ID_Imovel"])

#QUESTÃO 23
teste= df[df['Cidade'] == 'Teste'].index
df = df.drop(index=teste)

#QUESTÃO 24
df_agrupado = df.groupby(["Cidade"]).mean()