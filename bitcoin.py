import requests
import sys

# import json
API_KEY = "53e1505bde5d512cee2d33f9c3993ec0b38a814d3bb492d86a48fabca056ebdf"


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    try:
        fl_coin = float((sys.argv[1]))
        # print(fl_coin)
    except ValueError:
        sys.exit("Command-line argument is not a number")

    bitcoinvalue(fl_coin)


def bitcoinvalue(n):
    try:
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        # parameters = {"search": "bitcoin", "ids": "bitcoin"}
        response = requests.get(url)
        response.raise_for_status()  # It will check for status code. If not Success codes(200 - 299) then raises an excpetion.
        data = response.json()
        print(data)
        price = data["data"]["priceUsd"]
        user_cost = float(price) * n
        print(f"${user_cost:,.4f}")
    except requests.RequestException:
        sys.exit("Network Error")


main()
