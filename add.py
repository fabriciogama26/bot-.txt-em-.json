import json
import os
import zipfile
from os import path

dictcolecao = {}
dictcardprice = {}

price = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Price\\")

card = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\Cards\\")

trade = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\collection\\")

ListPriceCards = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\price-history\\cards-price.xls")

def __init__():

    for arquivos in os.listdir(price):
        zipfullprice = zipfile.ZipFile(price + arquivos)
        zipfullprice.extractall(price)
        zipfullprice.close()
        os. remove(price + arquivos) 
        for arq in os.listdir(price):
            pricecard = open(os.path.join(price, arq),"r")
            prices = json.load(pricecard)

    for arquivos2 in os.listdir(card):
        zipfullcard = zipfile.ZipFile(card + arquivos2)
        zipfullcard.extractall(card)
        zipfullcard.close()
        os. remove(card + arquivos2) 
        for arq2 in os.listdir(card):
            cards = open(os.path.join(card, arq2),"r")
            listcards = json.load(cards)

    for arquivos3 in os.listdir(trade):
        tradecards = open(os.path.join(trade, arquivos3),"r")
        for i in tradecards:
            key, desc = i.lstrip().split(None,1)
            dictcolecao[f"{desc.strip()}"] = dict(Number=key.strip())

    for full, pricefull  in zip(listcards, prices.items()):

        pricecard = pricefull[1]
        
        dictcardprice[full] = dict(listcards[f'{full}'], price=pricecard)

    with open(ListPriceCards, 'w') as nlc:
        
        new = json.dump(dictcardprice, nlc, indent=2)              
        nlc.write(str(new))
        nlc.close()

    os. remove(price + arq) 
    os. remove(card + arq2) 