import requests
from time import sleep
import main


def __init__():
                  
    ''' checar conexão de internet '''
    url = "https://www.goatbots.com/download-prices"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        main.__init__()
        
    except:
        sleep(60)
        return __init__()