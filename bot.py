import pyautogui
import webbrowser as wb
from time import sleep
from add import price, card, collectionprice

def __init__():

    try:

        wb.open("https://www.goatbots.com/download-prices")

        sleep(2)

        pyautogui.click(x=239, y=509)

        sleep(2)

        pyautogui.click(x=400, y=39)

        sleep(2)

        pyautogui.write(price)

        pyautogui.press("ENTER")

        pyautogui.click(x=525, y=439)

        sleep(2)

        pyautogui.click(x=189, y=486)

        sleep(2)

        pyautogui.click(x=400, y=39)

        sleep(2)

        pyautogui.write(card)

        pyautogui.press("ENTER")

        pyautogui.click(x=525, y=439)

        sleep(1)

        wb.open("https://www.goatbots.com/trade-history")

        sleep(2)

        pyautogui.click(x=742, y=305)

        sleep(2)

        pyautogui.click(x=400, y=39)

        sleep(2)

        pyautogui.write(collectionprice)

        pyautogui.press("ENTER")

        pyautogui.click(x=525, y=439)

    except:

        KeyError



