from .download import download_by_url
from ._internal import get_tree

BaseUrl = "https://docs.python.org/zh-cn/3/tutorial/index.html"
Base = "https://docs.python.org/zh-cn/3/tutorial/"


def run_app():
    print(" - - - Now Get Pages - - - ")
    toc = get_tree(BaseUrl)
    print("\n - - - Now Download Pages - - - ")
    for branch in toc.branches:
        download_by_url(Base + branch.url)
        print("")

    print("\nDownload succesful!")
