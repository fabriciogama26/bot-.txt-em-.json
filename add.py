import json

with open("C:\\Users\\Alpha\\Desktop\\PCMSO\\Cards_Price\\price-history\\price-history-2022-11-07.txt", "r") as p:

    prices = json.load(p)


with open("C:\\Users\\Alpha\\Desktop\\PCMSO\\Cards_Price\\price-history\\card-definitions.txt", "r") as c:

    cards = json.load(c)

dictcolecao = {}

with open("C:\\Users\\Alpha\\Desktop\\PCMSO\\Cards_Price\\price-history\\Full Trade List.txt") as co:
    for i in co:
        # key, desc = i.strip().split(None, 1)
        # dictcolecao[key] = desc.strip()

        print(i)


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