import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Process
import pandas as pd


URL_TEMPLATE = "https://bikepost.ru/"


def parse(url):
    result_list = {'name_author': [], 'topic': [], 'date': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    info = soup.find_all('div', class_="topic")
    for i in info:
        author_names = soup.find_all('li', class_='panel username')
        for name in author_names:
            result_list['name_author'].append(name.text)
    titles = soup.find_all('h2', class_="title")
    for i in titles:
        title_topics = soup.find_all('a', class_='title-topic')
        for topic in title_topics:
            result_list['topic'].append(topic.text)
    print(result_list)

def parse_author(url):
    result_list = {'name_author': [], 'topic': [], 'date': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    info = soup.find_all('div', class_="topic")
    for i in info:
        author_names = soup.find_all('li', class_='panel username')
        for name in author_names:
            result_list['name_author'].append(name.text)
    print(result_list)

def main():
    while True:
        p = Process(target=parse_author, args=(URL_TEMPLATE ,))
        p1 = Process(target=parse, args=(URL_TEMPLATE ,))
        p.start()
        p1.start()
        p.join()
        p1.join()

if __name__ == '__main__':
    main()
