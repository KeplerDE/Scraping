import csv
import json
import os
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

pages_count = 5


def collect_data(pages_count):
    for page in range(1, 2):
        with open(f"data/page_{page}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find_all(class_="product-item")  # первый передаем тег, второй класс
        # print(items_cards)  # анализируем код, нужно вернуть название и цену


        for item in items_cards:
            name = item.find("strong", class_="product-name").text.strip()
            price_old = item.find("span", class_="price").text.strip()
            # price_new = item.find(id="product-price-339500").text.strip()
            product_url = item.find("a", {"class": "product-item-photo"}).get("href")

            print(f"Article: {name} - Price: {price_old} - URL: {product_url}")


    return pages_count


collect_data(pages_count=pages_count)
