import requests
from bs4 import BeautifulSoup

url = 'https://afisha.tut.by/film/?crnd=49574'
r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")
link = soup.find('div', id='events-block')
links = link.find_all('li', class_='lists__li')


def main():
    return links
