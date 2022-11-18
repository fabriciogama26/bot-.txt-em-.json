import schedule
from time import sleep
import conexao

def __init__():

    try:

        schedule.every().day.at("09:50").do(conexao.__init__())
        schedule.run_pending() 
        sleep(60)      

    except:
        sleep(1)
        print("erro hora")
        return __init__()

if __name__=="__main__":
    __init__()

