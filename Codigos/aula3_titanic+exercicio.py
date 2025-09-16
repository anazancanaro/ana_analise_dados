# Exploração inicial dos dados

# Carregue o dataset no Pandas.
import pandas as pd
df = pd.read_csv("C:\\Users\\ana\\OneDrive\\Área de Trabalho\\IBMEC\\Semestre_4\\Analise_Dados\\Arquivos\\titanic.csv")

# Verifique o tamanho do dataset (linhas e colunas).
df.head()
df.shape
df.sample()

# Liste os nomes das colunas e os tipos de dados.
df.info()
df.columns
df.dtypes

# Descubra se há valores nulos e quantos por coluna.
df.isna().sum()

# Identifique quais colunas têm valores nulos (NaN) 
# e Substitua valores ausentes de:

# Age: pela média ou mediana da idade.
media_idade = df["Age"].mean()
df["Age"] = df["Age"].fillna(media_idade)
# df["Age"] = df["Age"].dropna()

# Embarked: pelo valor mais frequente. *embarked nao tem N/A
filtro_na = df["Fare"].isna()
df.loc[filtro_na]
moda_fare = df["Fare"].mode()
df["Fare"] = df["Fare"].fillna(moda_fare)

# Cabin: crie uma nova coluna HasCabin (1 com cabine, 0 sem)
df["HasCabin"] = df["Cabin"].notnull().astype(int)

# Criação de variáveis derivadas

# Crie uma coluna FamilySize = SibSp + Parch + 1.
df["FamilyMembers"] = df["SibSp"] + df["Parch"] + 1
df["FamilySize"] = df["FamilyMembers"]

# Crie uma coluna Title a partir do Name (ex.: Mr., Mrs., Miss., Master)
df["Title"] = df["Name"].str.split(",").str[1].str.split(".").str[0].str.strip()

# Transforme Sex em variável numérica (male=0, female=1).
df["Sex"] = df["Sex"].replace(
    {"male": 0,
     "female": 1}
)

# Estatísticas descritivas

# Calcule a idade média dos sobreviventes vs não sobreviventes.
df.groupby("Survived")["Age"].mean()

filtro_sob = df["Survived"] == 1
df_sob = df.loc[filtro_sob]
df_sob["Age"].mean()

filtro_nsob = df["Survived"] == 0
df_nsob = df.loc[filtro_nsob]
df_nsob["Age"].mean()

# Compare a tarifa média (Fare) entre as classes Pclass.
df.groupby('Pclass')['Fare'].mean()

# Verifique se havia diferença de sobrevivência por sexo 
# (taxa de sobrevivência homens x mulheres).
filtro_mulher_sob = (df["Sex"]==1) & (df["Survived"]==1)
df_mulher_sob = df.loc[filtro_mulher_sob]
qtd_mulher_sob = len(df_mulher_sob)

mulher_total = df["Sex"].value_counts()[1]

taxa_sob_mulher = qtd_mulher_sob/mulher_total
print(taxa_sob_mulher)

#
filtro_homem_sob = (df["Sex"]==0) & (df["Survived"]==1)
df_homem_sob = df.loc[filtro_homem_sob]
qtd_homem_sob = len(df_homem_sob)

homem_total = df["Sex"].value_counts()[0]

taxa_sob_homem = qtd_homem_sob/homem_total
print(taxa_sob_homem)

# Visualizações
# Faça um histograma da idade dos passageiros. 
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma da Idade dos Passageiros')
plt.xlabel('Idade')
plt.ylabel('Número de Passageiros')
plt.show()

# Faça um boxplot comparando Fare entre as classes (Pclass)
import seaborn as sns

plt.figure(figsize=(8,5))
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Boxplot da Tarifa (Fare) por Classe (Pclass)')
plt.xlabel('Classe (Pclass)')
plt.ylabel('Tarifa (Fare)')
plt.show()

# Qual foi a taxa de sobrevivência de:

# Passageiros com família grande (FamilySize >= 4) 
# vs pequenos (FamilySize < 4)?
filtro_grande_sob = (df["FamilySize"]>=4) & (df["Survived"]==1)
df_grande_sob = df.loc[filtro_grande_sob]
qtd_grande_sob = len(df_grande_sob)

fam_grande = (df["FamilySize"] >= 4).sum()

taxa_sob_grande = qtd_grande_sob/fam_grande
print(taxa_sob_grande)

filtro_fampeq_sob = (df["FamilySize"]<=4) & (df["Survived"]==1)
df_fampeq_sob = df.loc[filtro_fampeq_sob]
qtd_fampeq_sob = len(df_fampeq_sob)

fam_peq = (df["FamilySize"] <= 4).sum()

taxa_sob_fampeq = qtd_fampeq_sob/fam_peq
print(taxa_sob_fampeq)

# Passageiros de primeira classe vs terceira classe?
filtro_1_sob = (df["Pclass"] == 1) & (df["Survived"] == 1)
df_1_sob = df.loc[filtro_1_sob]
qtd_1_sob = len(df_1_sob)

total_1 = (df["Pclass"] == 1).sum()

taxa_sob_1 = qtd_1_sob / total_1

filtro_3_sob = (df["Pclass"] == 3) & (df["Survived"] == 1)
df_3_sob = df.loc[filtro_3_sob]
qtd_3_sob = len(df_3_sob)

total_3 = (df["Pclass"] == 3).sum()

taxa_sob_3 = qtd_3_sob / total_3

# Houve diferença de idade entre homens que sobreviveram 
# e que não sobreviveram?
filtro_homem_sob = (df["Sex"] == 0) & (df["Survived"] == 1)
idade_homem_sob = df.loc[filtro_homem_sob, "Age"].mean()

# Homens que não sobreviveram
filtro_homem_nsob = (df["Sex"] == 0) & (df["Survived"] == 0)
idade_homem_nsob = df.loc[filtro_homem_nsob, "Age"].mean()