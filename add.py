import json
import os
from os import path

dictcolecao = {}

price = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\txt-json.py\\Price\\")
card = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\txt-json.py\\Cards\\")
trade = path.join(path.expanduser("~"), "Desktop\\Cards_Price\\txt-json.py\\price-history\\")


for arquivos in os.listdir(price):
    pricecard = open(os.path.join(price, arquivos),"r")
    prices = json.load(pricecard)

for arquivos2 in os.listdir(card):
    cards = open(os.path.join(card, arquivos2),"r")
    listcards = json.load(cards)

for arquivos3 in os.listdir(trade):
    tradecards = open(os.path.join(trade, arquivos3),"r")
    for i in tradecards:
        key, desc = i.lstrip().split(None,1)
        dictcolecao[f"{desc.strip()}"] = dict(Number=key.strip())

print(dictcolecao)


# with open("C:\\Users\\Alpha\\Desktop\\PCMSO\\Cards_Price\\price-history\\Full_Trade_List.txt", "w") as col:
#     json.dump(dictcolecao, col, indent=2)
#     col.close()


# for cardcolecao in colecao


# dictcardprice = {}


# for cod, price, card, foil in zip(cards, prices.items(), cards.items(), cards.items()):

#     codcard = cod
#     namecard = card[1]["name"]
#     pricecard = price[1]
#     # cardset = ed[1]["cardset"]
#     cardfoil = foil[1]["foil"]
#     dictcardprice[f'{cod}'] = dict(name=namecard, price=pricecard, foil=cardfoil) 

            
# with open("C:\\Users\\Alpha\\Desktop\\PCMSO\\Cards_Price\\price-history\\cards-price.xls", "w") as cp:

#     new = json.dump(dictcardprice, cp, indent=2)
                    
#     cp.write(str(new))

#     cp.close()