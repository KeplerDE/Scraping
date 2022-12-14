# import csv
# import json
# import os
# import time
# import requests
from bs4 import BeautifulSoup
# from datetime import datetime

pages_count = 5


def collect_data():
    for page in range(1, 2):
        with open(f"data/page_{page}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find("div", class_="products")  # первый передаем тег, второй класс, для родительского блока
        print(items_cards)  # анализируем код, нужно вернуть название и цену

        for item in items_cards:
            name = item.find("strong", class_="product-name").text.replace(' ', '')
            print(name)



# //////////////////////////////////











        # for item in items_cards:
            # name = item.find("strong", class_="product-name").text.replace(' ', '')
            # price = item.find('span', {"class": "price"}).text.strip()
            # price_old = item.find("span", class_="rrp-price").text.strip()
            # product_url = item.find("a", {"class": "product-item-photo"}).get("href")

            # print(price)
            # print(name)


            # print(f"Article: {name} - Price: {price_old} - URL: {product_url}")

def main():
    collect_data()


if __name__ == '__main__':
    main()
