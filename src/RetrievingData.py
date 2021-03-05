from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote


class RetrievingData:
    def __init__(self, df):
        self.df = df

    def GetRatings(self, title):
        try:
            parsed_title = quote(title)
            findUrl = "https://www.imdb.com/find?q=" + parsed_title
            list_of_titles_page = request.urlopen(findUrl)
            soup = BeautifulSoup(list_of_titles_page, 'html.parser')
            table = soup.find('td', class_='result_text')
            link_to_the_show = table.find('a')['href']

            show_url = 'https://www.imdb.com/' + link_to_the_show
            show = request.urlopen(show_url)
            soup = BeautifulSoup(show, 'html.parser')
            rating_tag = soup.find('div', class_='ratingValue')
            ratings_text = rating_tag.find('strong')['title'].split()
            rating, user_count = float(ratings_text[0]), int(ratings_text[3].replace(',', ''))
            return [rating, user_count]
        except:
            return [0, 0]

    def addRatings(self, title="netflix_titles_with_ratings.csv"):
        ratings, users = [], []
        count = 0
        for i in range(self.df.shape[0]):
            r = RetrievingData().GetRatings(self.df['title'][i])
            ratings.append(r[0])
            users.append(r[1])
            if r == [0, 0]:
                count += 1
        self.df['user_rating'] = ratings
        self.df['users_count'] = users
        self.df.to_csv(title)
        print("Done")
        print(f"Successfully Retrieved: {self.df.shape[0] - count} / {self.df.shape[0]} and stored in '{title}'")

