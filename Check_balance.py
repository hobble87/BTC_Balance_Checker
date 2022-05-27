import pandas
import requests
import json



link = "https://api-r.bitcoinchain.com/v1/address/"

with open('Wallet.txt') as wallets_file:
    for line in wallets_file:
        target = line
        try:
            df = pandas.read_json(link + target)
            amount = df
            print(amount['address'].values[0], "BTC balance = ", amount['balance'].values[0])
            #print(amount['balance'].values[0])
            if (amount['balance'].values[0] > 0.001):
                f = open("hits.txt", 'a')
                f.write(line)
                f.close()
            else:
                print("No Balance")
        except:
            pass
