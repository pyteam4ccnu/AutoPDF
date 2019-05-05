from .download import download_by_url
from ._internal import get_tree
import os

BaseUrl = os.environ.get("AutoPDF_BaseUrl") or "https://docs.python.org/zh-cn/3/tutorial/index.html"
Base = os.environ.get("AutoPDF_Base") or "https://docs.python.org/zh-cn/3/tutorial/"


def run_app():
    """
    This function means to run all step of download pdf: get doc tree and download.
    :return:
    """
    print(" - - - Now Get Pages - - - ")
    toc = get_tree(BaseUrl)
    print("\n - - - Now Download Pages - - - ")
    for branch in toc.branches:
        download_by_url(Base + branch.url)
        print("")

    print("\nDownload succesful!")
