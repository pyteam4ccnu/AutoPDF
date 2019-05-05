from .driver import driver
from .decorator.timer import Timer

@Timer
def download_by_url(url):
    driver.get(url)
    driver.execute_script('window.print();')