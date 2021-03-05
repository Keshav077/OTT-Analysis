import pandas as pd
from src import Visualization, RetrievingData, Analysis, HandlingMissingData
import tkinter as tk

x, y, h, w, b = 0.5, 0.04, 2, 25, 12
color = "white"


r = tk.Tk()
r.geometry('500x600')
r.title('OTT Recommendation')
r.config(background="grey10")
label = tk.Label(r, text="OTT RECOMMENDATION", font=("Helvetica", 25, "bold"), bg="grey10", fg="white")
label.place(relx=x, rely=0.04, anchor=tk.CENTER)

# df = pd.read_csv("../netflix_titles.csv")
df = pd.read_csv("../netflix_titles_with_ratings.csv")
# RetrievingData.addRatings(df)

preprocess = HandlingMissingData.HandlingMissingValues(df)

df = Analysis.convertDate(df)

df['length'] = df.apply(Analysis.duration, axis=1)


m = df['users_count'].quantile(0.9196)
C = df['user_rating'].mean()



def weighted_ratings(row):
    v = row['users_count']
    R = row['user_rating']

    return round((v / (v + m) * R) + (m / (m + v) * C), 2)


top_rated = df.copy().loc[df['users_count'] > m]
top_rated['w_ratings'] = top_rated.apply(weighted_ratings, axis=1)
top_rated = top_rated.sort_values('w_ratings', ascending=False)

total_tv_content = Analysis.getType(df.copy(), 'TV Show')
top_tv_content = Analysis.getType(top_rated.copy(), 'TV Show')

total_movie_content = Analysis.getType(df.copy(), 'Movie')
top_movie_content = Analysis.getType(top_rated.copy(), 'Movie')

top_tv_genreRatios = Analysis.getGenreRatio(top_tv_content)

top_movie_genreRatios = Analysis.getGenreRatio(top_movie_content)

# Creating GUI
button = tk.Button(r,
                   text='Data Set Info',
                   height=h,
                   width=w,
                   font=("Helvetica", b),
                   relief="flat",
                   bg=color,
                   command=lambda: preprocess.showDataSetInfo())
button.place(relx=x, rely=y+0.1, anchor=tk.CENTER)

button2 = tk.Button(r,
                    text='Missing Data Graph',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: Visualization.showMissingDataGraph(preprocess.df))
button2.place(relx=x, rely=y+0.2, anchor=tk.CENTER)

button3 = tk.Button(r,
                    text='Missing Data Percentage',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: preprocess.showMissingDataPercentage())
button3.place(relx=x, rely=y+0.3, anchor=tk.CENTER)

button4 = tk.Button(r,
                    text='Handle Missing Data',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: preprocess.handleMissingValues(['director', 'date_added']))
button4.place(relx=x, rely=y+0.4, anchor=tk.CENTER)

button5 = tk.Button(r,
                    text='Type Ratio',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: Visualization.TypeRatio(top_rated))
button5.place(relx=x, rely=y+0.5, anchor=tk.CENTER)

button6 = tk.Button(r,
                    text='Movie Length Graph',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: Visualization.movieLengthGraph(
                        top_movie_content['length'].value_counts().sort_index(),
                        total_movie_content['length'].value_counts().sort_index()))
button6.place(relx=x, rely=y+0.6, anchor=tk.CENTER)

button7 = tk.Button(r,
                    text='TV Show Length Graph',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: Visualization.tvShowLengthGraph(
                        top_tv_content['length'].value_counts().sort_index(),
                        total_tv_content['length'].value_counts().sort_index()))
button7.place(relx=x, rely=y+0.7, anchor=tk.CENTER)

button8 = tk.Button(r,
                    text='Top TV Show Genre Ratio',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: Visualization.showGenreRatio(top_tv_genreRatios, "TV Show"))
button8.place(relx=x, rely=y+0.8, anchor=tk.CENTER)

button9 = tk.Button(r,
                    text='Top Movie Genre Ratio',
                    height=h,
                    width=w,
                    font=("Helvetica", b),
                    bg=color,
                    command=lambda: Visualization.showGenreRatio(top_movie_genreRatios, "Movie"))
button9.place(relx=x, rely=y+0.9, anchor=tk.CENTER)

r.mainloop()
