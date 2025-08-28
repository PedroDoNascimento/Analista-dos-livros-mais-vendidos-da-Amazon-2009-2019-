import pandas as pd

ler_arquivo = pd.read_csv('bestsellers with categories.csv')

print(ler_arquivo.head())
print(ler_arquivo.shape)
print(ler_arquivo.columns)
print(ler_arquivo.describe())

ler_arquivo.drop_duplicates(inplace=True)

ler_arquivo.rename(columns={"Name": "Titulo", "Year": "Ano de Publicação", "User Rating": "Avaliação"}, inplace=True)

ler_arquivo["Price"] = ler_arquivo["Price"].astype(float)

author_counts = ler_arquivo['Author'].value_counts()
print(author_counts)

avg_rating_by_genre = ler_arquivo.groupby("Genre")["Avaliação"].mean()
print(avg_rating_by_genre)

#Exportando o DataFrame para planilha 

author_counts.head(10).to_csv("top_authors.csv")

avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
