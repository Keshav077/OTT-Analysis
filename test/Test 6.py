import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv("../netflix_titles_with_ratings.csv")
df = pd.read_csv("../top_content.csv")


def dur(x):
    return int(x['duration'].split()[0])


def getType(df, type):
    return df.loc[df['type'] == type]


df['dur'] = df.apply(dur, axis=1)
d['dur'] = d.apply(dur, axis=1)

total_tv_shows = getType(d, "TV Show")
total_movies = getType(d, "Movie")

top_tv_shows = getType(df, "TV Show")
top_movies = getType(df, "Movie")

top_movie_duration = top_movies['dur'].value_counts().sort_index()
total_movie_duration = total_movies['dur'].value_counts().sort_index()

top_tv_show_duration = top_tv_shows['dur'].value_counts().sort_index()
total_tv_show_duration = total_tv_shows['dur'].value_counts().sort_index()


def movieLengthGraph(top_content, total_content, barWidth=0.5):
    plt.figure(figsize=(10, 5))
    plt.bar(top_content.index, top_content, color='r', width=barWidth, label='Top 500')
    plt.bar([x+barWidth for x in total_content.index], total_content, color='g', width=barWidth, label='Total Entries')
    plt.ylabel('No. of Movies', fontweight='bold')
    plt.xlabel('Minutes', fontweight='bold')
    plt.legend()
    plt.show()


def tvShowLengthGraph(top_content, total_content, barWidth=0.5):
    plt.figure(figsize=(10, 5))
    plt.bar(top_content.index, top_content, color='r', width=barWidth, label='Top 500')
    plt.bar([x+barWidth for x in total_content.index], total_content, color='g', width=barWidth, label='Total Entries')
    plt.ylabel('No. of TV Shows', fontweight='bold')
    plt.xlabel('Seasons', fontweight='bold')
    plt.xticks([i+barWidth-0.25 for i in range(1, 16)], [i for i in range(1, 16)])
    plt.legend()
    plt.show()


def TypeRatio(df):
    plt.figure(figsize=(10, 5))
    plt.pie(df['type'].value_counts(), labels=df['type'].value_counts().index,
            explode=[0.05, 0], autopct='%1.2f%%', colors=['Orange', 'Red'])
    plt.title("Top Content Ratio", fontsize=20)
    plt.show()


def showGenreRatio(genre_percentage, Title):
    plt.figure(figsize=(10, 7))
    plt.pie(genre_percentage[1], labels=genre_percentage[0], autopct='%1.2f%%', colors=sns.color_palette("RdGy", n_colors=20))
    plt.title(f"{Title} Genre Ratio's")
    plt.show()


def monthlyAnalysisGraph(total_content, top_content, barWidth=0.5):
    top_month_count = top_content['month_added'].value_counts().sort_index()
    total_month_count = total_content['month_added'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(total_month_count.index, total_month_count, color='r', label='Total Entries')
    plt.plot([x + barWidth for x in top_month_count.index], top_month_count, color='g', label='Top 500')
    plt.xlabel('Month', fontweight='bold')
    plt.ylabel('No. of Shows Released', fontweight='bold')
    plt.xticks([r for r in range(1, 13)], ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])
    plt.legend()
    plt.show()
