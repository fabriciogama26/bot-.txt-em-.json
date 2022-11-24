import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
# import requests
from time import sleep
from add import card, price




def __init__():

    global options

    global navegador

    options = Options()
    options.headless = False

    navegador = uc.Chrome(options = options)

    # options = webdriver.ChromeOptions()

    # options.add_argument('proxy-server=106.122.8.54:3128')
    # ou usar
    # options.add_argument('--user-data-dir=C:\Users\suppo\AppOata\Local\Google\Chrome\User Data\Default')

    # browser = uc.Chrome(
    # options=options)

    link = "https://www.goatbots.com/download-prices"

    navegador.get(url=link)
    sleep(2)

    # /price-history.zip?2022-11-19'
    # /card-definitions.zip?2022-11-19'

    # linkDados = navegador.find_element(by=By.XPATH,value='//*[@id="main"]/ul[1]/li[2]/a').get_attribute("href")
    link1 = navegador.find_element(by=By.XPATH,value='//*[@id="main"]/ul[1]/li[2]/a')

    options.add_argument(f"download.default_directory={price}")

    link1.click()

    sleep(1)

    link2 = navegador.find_element(by=By.XPATH,value='//*[@id="main"]/ul[1]/li[1]/a')

    options.add_argument(f"download.default_directory={card}")

    link2.click()

    # sleep(1)

    # link = "https://www.goatbots.com/trade-history"

    # navegador.get(url=link)
    # sleep(2)

    # link3 = navegador.find_element(by=By.XPATH,value='//*[@id="main"]/p/a')

    # options.add_argument(f"download.default_directory={collectionprice}")

    # link3.click()


# def download_file(urls, local_filename):
#     with requests.get (urls, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return local_filename


if __name__== '__main__':
    __init__()
