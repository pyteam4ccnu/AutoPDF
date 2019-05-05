from .driver import driver
from .decorator.timer import Timer

@Timer
def download_by_url(url):
    """
    This function make the simple action: download.
    :param url: url for download pdf.
    :return:
    """
    driver.get(url)
    driver.execute_script('window.print();')