import requests
from time import sleep
import botscrap, add, bot

def __init__():

                  
    ''' checar conexão de internet '''
    url = "https://www.goatbots.com/download-prices"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        bot.__init__()
        add.__init__()  

    except:
        sleep(60)
        return __init__() 

if __name__ == "__main__":
    __init__()