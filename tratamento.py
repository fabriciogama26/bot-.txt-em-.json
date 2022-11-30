import pandas as pd
from glob import glob


arquivos = sorted(glob('price-history\semana 2\*.json'))

df = pd.DataFrame()

for arquivo in arquivos:
    df = pd.concat([df, pd.read_json(arquivo, orient='index')])

    df.reset_index(drop=False).rename({'index':'id'}, axis=1).head()

df.to_csv("analise.csv")




