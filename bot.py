import pyautogui
import webbrowser as wb
from time import sleep
from add import price, card, collectionprice

def __init__():

    try:

        wb.open("https://www.goatbots.com/download-prices")

        sleep(3)

        #dowload
        pyautogui.click(x=239, y=509)

        sleep(3)

        #local
        pyautogui.click(x=398, y=156)

        sleep(3)

        pyautogui.write(price)

        sleep(1)

        pyautogui.press("ENTER")

        #salvar
        pyautogui.click(x=537, y=554)

        sleep(3)

        #dowload
        pyautogui.click(x=189, y=486)

        sleep(3)

        #local
        pyautogui.click(x=398, y=156)

        sleep(3)

        pyautogui.write(card)

        sleep(1)

        pyautogui.press("ENTER")

        #salvar
        pyautogui.click(x=537, y=554)

        sleep(1)

        wb.open("https://www.goatbots.com/trade-history")

        sleep(3)

        #dowload
        pyautogui.click(x=742, y=305)

        sleep(3)

        #local
        pyautogui.click(x=398, y=156)

        sleep(3)

        pyautogui.write(collectionprice)

        sleep(1)

        pyautogui.press("ENTER")

        #salvar
        pyautogui.click(x=537, y=554)

    except:

        KeyError



