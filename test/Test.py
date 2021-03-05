import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored

df = pd.read_csv("../netflix_titles_with_ratings.csv")

C = df['user_ratings'].mean()

m = df['users_count'].quantile(0.9196)


def weighted_ratings(x, C, m):
    v = x['users_count']
    R = x['user_ratings']

    return round((v/(v+m) * R) + (m/(m+v) * C), 2)


top_rated = df.copy().loc[df['users_count'] > m]
# print(top_rated.shape)


top_rated['w_ratings'] = top_rated.apply(weighted_ratings, axis=1)
top_rated = top_rated.sort_values('w_ratings', ascending=False)
top_rated = top_rated.loc[:, 'show_id':'w_ratings']
# top_rated.loc[:, ['show_id', 'title', 'type', 'genre', 'user_ratings', 'users_count', 'w_ratings']].to_csv(
# 'top_content.csv', index=False)



'''
top_rated["date_added"] = pd.to_datetime(top_rated['date_added'])
top_rated['month_added'] = top_rated['date_added'].dt.month
top_rated['month_name_added'] = top_rated['date_added'].dt.month_name()
top_rated['year_added'] = top_rated['date_added'].dt.year

top_rated.to_csv('top_content.csv', index=False)
top_tv = top_rated.copy().loc[top_rated['type'] == 'TV Show']
top_movie = top_rated.copy().loc[top_rated['type'] == 'Movie']
'''