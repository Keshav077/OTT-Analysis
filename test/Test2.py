from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote
import pandas as pd


def GetRatings(title):
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
        ratings, users = float(ratings_text[0]), int(ratings_text[3].replace(',', ''))
        return [ratings, users]
    except:
        return [0, 0]


print(GetRatings("123abc"))
