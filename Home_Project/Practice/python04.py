from urllib import response

import requests
import pandas as pd


def printline():
    print("=" * 50)


def get_gold_price():
    url = "https://api.chnwt.dev/thai-gold-api/latest"
    response = requests.get((url))
    data = response.json()
    gold_price = data["response"]["price"]
    df = pd.DataFrame(gold_price)
    printline()
    print("Recent Gold Price in Thailand")
    printline()
    print(df)
    printline()


if __name__ == "__main__":
    get_gold_price()
