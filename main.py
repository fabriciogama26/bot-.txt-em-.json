import pyautogui
import webbrowser as wb
from time import sleep
import add
from add import price, card
import conexao

def __init__():

    try:

        wb.open("https://www.goatbots.com/download-prices")

        sleep(3)

        pyautogui.click(x=239, y=509)

        sleep(3)

        pyautogui.click(x=400, y=39)

        sleep(2)

        pyautogui.write(price)

        pyautogui.press("ENTER")

        pyautogui.click(x=525, y=439)

        sleep(3)

        pyautogui.click(x=189, y=486)

        sleep(3)

        pyautogui.click(x=400, y=39)

        sleep(2)

        pyautogui.write(card)

        pyautogui.press("ENTER")

        pyautogui.click(x=525, y=439)

        sleep(3)

    except:

        KeyError

if __name__=="__main__":
    conexao.__init__()
    add.__init__()

