# EXERCÍCIO PANDAS MYNTRA DATAFRAME

import pandas as pd

df = pd.read_csv("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\myntra_dataset_ByScraping.csv")

df.head()
df.tail()

df.shape

df.columns

df.dtypes

df.info()

df["brand_name"].unique()

filter = (df["price"]>= 1000) & (df["price"]<= 3000)
df1 = df.loc[filter]

df2 = df[["brand_name","pants_description","price"]]

filter = df["brand_name"]=="Roadster"
df_roadster = df.loc[filter]

df.isnull().sum()

df.sort_values(["price"], ascending=False)

med = df["price"].mean()

df["price"].median()

df["price"].std()

df["discount_percent"].max()
df["discount_percent"].min()

df_menor = df["price"]<med
df_maior = df["price"]>med

df_menor.value_counts()
df_maior.value_counts()

df["preco_desconto"]= df["MRP"]*(1-df["discount_percent"])

filter = df["ratings"] < 2
df = df.drop(df[filter].index)

df.drop(["pants_description"], axis = 1)

df.groupby("brand_name")["price"].mean()

# EXERCÍCIO CONCAT E MERGE MYNTRA DATAFRAME

#1
dados_novos_produtos = {
    "brand_name": ["Myntra Basics", "Denim Pro", "Urban Style"],
    "pants_description": [
        "Men Slim Fit Blue Jeans",
        "Men Regular Fit Jeans",
        "Men Tapered Fit Jeans"
    ],
    "price": [1299, 1599, 1899],
    "MRP": [1999, 2499, 2899],
    "discount_percent": [0.35, 0.40, 0.34],
    "ratings": [4.1, 3.8, 4.3],
    "number_of_ratings": [23, 12, 47]
}
df_novos = pd.DataFrame(dados_novos_produtos)
df = pd.concat([df, df_novos])


#2
dados_promocoes = {
    "brand_name": ["Test Brand A", "Test Brand B", "Test Brand C"],
    "pants_description": [
        "Men Slim Fit Black Jeans",
        "Men Regular Fit Grey Jeans",
        "Men Loose Fit White Jeans"
    ],
    "discount_percent": [0.50, 0.60, 0.45]
}

df_promocoes = pd.DataFrame(dados_promocoes)
df = pd.concat([df, df_promocoes], axis = 0)
df = pd.concat([df, df_promocoes], axis = 1)


#3
dados_marcas_info = {
    "brand_name": ["Roadster", "WROGN", "Flying Machine", "Urban Style"],
    "country": ["India", "India", "USA", "Brazil"],
    "year_founded": [2012, 2014, 1980, 2018]
}
df_extra = pd.DataFrame(dados_marcas_info)
pd.merge(df, df_extra, on = "brand_name", how = "inner")


#4
dados_categorias = {
    "pants_description": [
        "Men Slim Fit Jeans",
        "Men Regular Fit Jeans",
        "Men Loose Fit Cotton Jeans",
        "Men Tapered Fit Jeans"
    ],
    "category": ["Slim", "Regular", "Loose", "Tapered"]
}
df_categ = pd.DataFrame(dados_categorias)
df_novo = pd.merge(df, df_categ, on = "pants_description", how = "inner")


#5
dados_ratings_extra = {
    "brand_name": ["Roadster", "WROGN", "Urban Style"],
    "avg_new_rating": [4.0, 4.3, 4.1]
}
df_ratings = pd.DataFrame(dados_ratings_extra)
df_novo = pd.merge(df, df_ratings, on = "brand_name", how = "left")
df_novo = [["ratings", "avg_new_rating"]]