from .download import download_by_url
from ._internal import get_tree
import os

BaseUrl = "https://docs.python.org/3.8/library/asyncio.html#module-asyncio" # os.environ.get("AutoPDF_BaseUrl") or "https://docs.python.org/zh-cn/3/tutorial/index.html"
Base = "https://docs.python.org/3.8/library/" # os.environ.get("AutoPDF_Base") or "https://docs.python.org/zh-cn/3/tutorial/"


def run_app(base_url=None, base=None):
    """
    This function means to run all step of download pdf: get doc tree and download.
    :return:
    """
    if not base_url and not base:
        base_url, base = BaseUrl, Base

    print(" - - - Now Get Pages - - - ")
    toc = get_tree(base_url)
    print("\n - - - Now Download Pages - - - ")
    for branch in toc.branches:
        download_by_url(base + branch.url)
        print("")

    print("\nDownload succesful!")
