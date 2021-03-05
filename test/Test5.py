import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


d = pd.read_csv("../netflix_titles_with_ratings.csv")
d["date_added"] = pd.to_datetime(d['date_added'])
d['month_added'] = d['date_added'].dt.month
d['month_name_added'] = d['date_added'].dt.month_name()
d['year_added'] = d['date_added'].dt.year


barWidth = 0.5
month = d['month_added'].value_counts().sort_index()


df = pd.read_csv("../top_content.csv")
# year_count = df['year_added'].value_counts().sort_index()
# month_count = df['month_added'].value_counts().sort_index()


def monthlyAnalysisGraph(df):
    month_count = df['month_added'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(month_count.index, month_count, color='r', label='Total Entries')
    plt.plot([x + barWidth for x in month.index], month, color='g', label='Top 500')
    plt.xlabel('Month', fontweight='bold')
    plt.ylabel('No. of Shows Released', fontweight='bold')
    plt.xticks([r for r in range(1, 13)], ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])
    plt.legend()
    plt.show()
# print(df['year_added'].value_counts())


'''top_tv = df.copy().loc[df['type'] == 'TV Show']
top_movie = df.copy().loc[df['type'] == 'Movie']'''

