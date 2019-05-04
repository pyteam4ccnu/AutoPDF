from driver import driver


def download_by_url(url):
    driver.get(url)
    driver.execute_script('window.print();')
