
#Importar a biblioteca e ler o arquivo
import pandas as pd
df = pd.read_csv("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\imoveis_brasil.csv")
#Análise exploratória dos dados
df.shape
df.columns
df.head(5)
df.info()

#Quais tipos de imóveis?
df["Tipo_Imovel"].unique()

#Imóveis maiores que R$1.000.000
filtro = df["Valor_Imovel"]>1000000
df.loc[filtro]
df_1M = df.loc[filtro]

#Outro df com colunas selecionadas
df2 = df[["Cidade", "Bairro", "Valor_Imovel"]]

#Ordenar, crescente (ascending = True) ou decrescente (ascending = False)
df.sort_values(["Valor_Imovel"], ascending=False)

#Valor medio dos imóveis
df["Valor_Imovel"].mean()

#Valor medio dos imóveis em Curitiba
filtro_curitiba = df["Cidade"]=="Curitiba"
df_cur = df.loc[filtro_curitiba, ["Valor_Imovel"]]
df_media = df_cur["Valor_Imovel"].mean()

#Quantidade de imóveis em curitiba
len(df_cur)

#Numero de imóveis acima do valor medio

filtro_acima_media = df["Valor_Imovel"] > df_media
df_acima_media = df.loc[filtro_acima_media]
len(df_acima_media)

#Numero de imóveis abaixo do valor medio

filtro_abaixo_media =  df["Valor_Imovel"] < df_media
df_abaixo_media = df.loc[filtro_abaixo_media]

len(df_abaixo_media)

