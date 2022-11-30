import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from add import price, card



def __init__():

    options = Options()

    options.headless = True

    navegador = uc.Chrome(options= options)

    link = "https://www.goatbots.com/download-prices"

    navegador.get(url=link)
    sleep(2)

    link1 = navegador.find_element(by=By.XPATH,value='//*[@id="main"]/ul[1]/li[2]/a')

    sleep(2)

    link1.click()

    sleep(2)

    link2 = navegador.find_element(by=By.XPATH,value='//*[@id="main"]/ul[1]/li[1]/a')

    options.add_argument(f"savefile.default_directory={card}")

    sleep(2)

    link2.click()

    sleep(2)


if __name__== '__main__':
    __init__()
