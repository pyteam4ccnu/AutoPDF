import requests
from doc_tree import DocTree
from bs4 import BeautifulSoup

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
}


def get_tree(url):
    session = requests.Session()
    session.headers = headers
    respones = session.get(url)
    soup = BeautifulSoup(respones.text, features="lxml")

    root = DocTree(url)
    level = 1
    titles = soup.find_all('li')
    references = soup.find_all(class_="reference internal")
    if len(titles) == len(references):
        print("Yes", len(titles))
    else:
        print("No", len(titles), len(references))
