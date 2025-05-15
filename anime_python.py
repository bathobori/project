import os
print(os.getcwd()) 

import pandas as pd

# Szerveres elérési útvonal
base_path = "/home/bartho-borbala/~anime/"

anime_path = base_path + "AnimeList.csv"
users_path = base_path + "UserList.csv"
ratings_path = base_path + "UserAnimeList.csv"

# Beolvasás
anime = pd.read_csv(anime_path)
ratings = pd.read_csv(ratings_path)
users = pd.read_csv(users_path)

# Összefűzés
df = ratings.merge(users, on="username", how="left")
df = df.merge(anime, on="anime_id", how="left")

# Ellenőrzés
print("Merged dataframe shape:", df.shape)
print("Columns:", df.columns.tolist())
