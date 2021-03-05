import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dfx = pd.read_csv("../top_content.csv")


def getGenreRatio(df):
    genres = {}
    for i in df['genre']:
        for j in i.split(','):
            x = j.strip()
            genres[x] = genres.get(x, 0) + 1
    total = sum(genres.values())
    for i in genres:
        genres[i] = (genres[i] / total) * 100
    return pd.DataFrame(sorted(genres.items(), key=lambda k: k[1], reverse=True))


d_tv = dfx.copy().loc[dfx['type'] == 'TV Show']
d_m = dfx.copy().loc[dfx['type'] == 'Movie']
tv_genres = getGenreRatio(d_tv)
movie_genres = getGenreRatio(d_m)


def showGenreRatio(genre_percentage, Title):
    plt.figure(figsize=(10, 7))
    plt.pie(genre_percentage[1], labels=genre_percentage[0], autopct='%1.2f%%', colors=sns.color_palette("RdGy", n_colors=20))
    plt.title(f"{Title} Genre Ratio's")
    plt.show()


showGenreRatio(tv_genres, "TV")
showGenreRatio(movie_genres, "Movie")
