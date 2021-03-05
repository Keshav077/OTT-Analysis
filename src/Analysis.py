import pandas as pd


def getGenreRatio(df):
    genres = {}
    for i in df['genre']:
        for j in i.split(','):  # Dramas : 10, Internation : 20
            x = j.strip()
            genres[x] = genres.get(x, 0) + 1
    total = sum(genres.values())
    for i in genres:
        genres[i] = (genres[i] / total) * 100
    return pd.DataFrame(sorted(genres.items(), key=lambda k: k[1], reverse=True))


def duration(x):
    if x['duration'] is not None:
        return int(x['duration'].split()[0])


def getType(df, show_type):
    return df.loc[df['type'] == show_type]


def convertDate(df):
    df["date_added"] = pd.to_datetime(df['date_added'])
    df['month_added'] = df['date_added'].dt.month
    df['year_added'] = df['date_added'].dt.year
    return df


