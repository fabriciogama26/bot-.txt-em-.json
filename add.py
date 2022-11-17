import json
import os
import zipfile
from os import path
import datetime
import csv

data = datetime.datetime.today()

dictcolecao = {}
dictcardprice = {}
dictcolecaoprice = {}

collectionprice = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Collectionprice\\")

collectionpricearquive = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Collectionprice\\goatbots-trade-history.csv")

collectionpricearquivenew = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Collectionprice\\goatbots_trade_history.txt")

price = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Price\\")

card = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Cards\\")

collection = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\collection\\")

dictcollection = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\collection\\Full_Trade_List.txt")

ListPriceCards = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\price-history\\cards-price" + "-" + f"{data.day}" + "-" + f"{data.month}"+ "-" + f"{data.year}"".txt")

def __init__():

    for arquivos in os.listdir(price):
        zipfullprice = zipfile.ZipFile(price + arquivos)
        zipfullprice.extractall(price)
        zipfullprice.close()
        os.remove(price + arquivos) 
        for arq in os.listdir(price):
            pricecard = open(os.path.join(price, arq),"r")
            prices = json.load(pricecard)
            pricecard.close()
            os.remove(price + arq) 

    for arquivos2 in os.listdir(card):
        zipfullcard = zipfile.ZipFile(card + arquivos2)
        zipfullcard.extractall(card)
        zipfullcard.close()
        os.remove(card + arquivos2) 
        for arq2 in os.listdir(card):
            cards = open(os.path.join(card, arq2),"r")
            listcards = json.load(cards)
            cards.close()
            os.remove(card + arq2) 

    for arquivos3 in os.listdir(collection):
        tradecards = open(os.path.join(collection, arquivos3),"r")
        for i in tradecards:
            key, desc = i.lstrip().split(None,1)
            dictcolecao[f"{desc.strip()}"] = dict(Number=key.strip())

    with open(collectionpricearquive) as csvFile:

        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            id = rows['itemID']
            dictcolecaoprice[id] = rows         

    for full, pricefull  in zip(listcards, prices.items()):

        pricecard = pricefull[1]
        
        dictcardprice[full] = dict(listcards[f'{full}'], price=pricecard)

    with open(dictcollection, 'w') as ftl:
                    
        ftl.write(str(json.dump(dictcolecao, ftl, indent=2)))
        ftl.close()

    with open(collectionpricearquivenew, 'w') as cpn:

        cpn.write(json.dumps(dictcolecaoprice, indent=4))
        cpn.close()
        os.remove(collectionpricearquive) 

    with open(ListPriceCards, 'w') as nlc:
              
        nlc.write(str(json.dump(dictcardprice, nlc, indent=2)))
        nlc.close()
