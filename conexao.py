import requests
from time import sleep
import bot, add

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

    


    
    
