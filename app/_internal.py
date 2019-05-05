import requests
from .doc_tree import DocTree
from bs4 import BeautifulSoup

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
}


def recursive(node_now, soup_now):
    """

    :param node_now: the doc tree node now, please make sure be init.ed
    :param soup_now: the html soup now, please make sure is a <ul>
    :return: new_node_now.
    """
    for tag in soup_now.children:
        if tag.name != "li":
            continue
        a = tag.a
        print("[Find]:", a['href'])
        new_children = DocTree(a['href'])
        if tag.ul is not None:
            new_children = recursive(new_children, tag.ul)
        node_now.branches.append(new_children)
    return node_now


def get_tree(url):
    session = requests.Session()
    session.headers = headers
    respones = session.get(url)
    soup = BeautifulSoup(respones.text, "html.parser")

    block = soup.find(class_="toctree-wrapper compound")

    root = DocTree(url)
    root = recursive(root, block.ul)
    print(len(root.branches))
    return root
