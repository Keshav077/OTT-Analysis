import pandas as pd

df = pd.read_csv("../netflix_titles_with_ratings.csv")
df = df.loc[:, "show_id":"users_count"]
df.to_csv("../netflix_titles_with_ratings.csv", index=False)
