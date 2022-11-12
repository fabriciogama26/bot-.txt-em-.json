import pyautogui
import webbrowser as wb
from time import sleep

wb.open("https://www.goatbots.com/download-prices")

sleep(3)

pyautogui.click(x=239, y=509)

sleep(3)

pyautogui.click(x=339, y=39)

sleep(3)

caminho = "C:\\Users\\Alpha\\Desktop\\PCMSO\\Cards_Price\\price-history"

pyautogui.write(caminho)

pyautogui.press("ENTER")

pyautogui.click(x=525, y=439)

sleep(3)

pyautogui.click(x=189, y=486)

sleep(3)

pyautogui.click(x=339, y=39)

sleep(3)

pyautogui.write(caminho)

pyautogui.press("ENTER")

pyautogui.click(x=525, y=439)
