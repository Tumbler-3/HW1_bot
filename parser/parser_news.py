import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.securitylab.ru/news/'

Headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    return requests.get(url=url, headers=Headers, params=params)


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('a', class_='article-card inline-card')
    news = []
    for item in items:
        new = {
            'headline': item.find('h2').string,
            'link': item.get('href'),
            'description': item.find('p').string,
        }
        news.append(new)
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_news = []
        for i in range(1, 2):
            html = get_html(f"{URL}page{i}_{i + 1}.php")
            current_page = get_data(html.text)
            all_news.extend(current_page)
        return all_news
