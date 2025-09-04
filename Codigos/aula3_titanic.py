import pandas as pd

df = pd.read_csv("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\titanic.csv")

df.head
df.columns
df.isna().sum()
df.shape
df.info()

#linhas com fare na
filtro_na = df["Fare"].isna()
df.loc[filtro_na]

#linhas com age na

filtro_na2 = df["Age"].isna()
df.loc[filtro_na2]

media_idade = df["Age"].mean()
df["Age"] = df["Age"].fillna(0)
df["Age"] = df["Age"].dropna()

#calcular a media de homens
filtro_homem = df["Sex"]=="male"
df_homem = df.loc[filtro_homem]
df_homem["Age"].mean()

#calcular a media das mulheres
filtro_homem = df["Sex"]=="female"
df_homem = df.loc[filtro_homem]
df_homem["Age"].mean()

#groupby
df.groupby("Sex")["Age"].mean()

#filtrar atraves de duas colunas

filtro_mulher_sob = (df["Sex"]=="female") & (df["Survived"]==1)
df_mulher_sob = df.loc[filtro_mulher_sob]
len(df_mulher_sob)

#criar uma coluna nova chamada "familymembers"

df["FamilyMembers"] = df["SibSp"] + df["Parch"] + 1

df["FamilyMembers"].mean()