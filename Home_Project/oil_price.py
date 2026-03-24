import requests
import pandas as pd

url = "https://api.chnwt.dev/thai-oil-api/latest"
response = requests.get(url)
data = response.json()


def ppt_oil_price():
    ptt = data["response"]["stations"]["ptt"]
    df_ptt = pd.DataFrame(ptt).T
    print("========== PTT Oil Price ==========")
    print(df_ptt.to_markdown(tablefmt="fancy_grid"))
    print()


def shell_oil_price():
    shell = data["response"]["stations"]["shell"]
    df_shell = pd.DataFrame(shell).T
    print("========== Shell Oil Price ==========")
    print(df_shell.to_markdown(tablefmt="fancy_grid"))
    print()


def bcp_oil_price():
    bcp = data["response"]["stations"]["bcp"]
    df_bcp = pd.DataFrame(bcp).T
    print("========== BCP Oil Price ==========")
    print(df_bcp.to_markdown(tablefmt="fancy_grid"))
    print()


def caltex_oil_price():
    caltex = data["response"]["stations"]["caltex"]
    df_caltex = pd.DataFrame(caltex).T
    print("========== Caltex Oil Price ==========")
    print(df_caltex.to_markdown(tablefmt="fancy_grid"))
    print()


if __name__ == "__main__":
    ppt_oil_price()
    shell_oil_price()
    bcp_oil_price()
    caltex_oil_price()
