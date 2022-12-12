import requests
from bs4 import BeautifulSoup
import os
import re
import time
import csv
from datetime import datetime


def get_all_pages():
    headers = {

        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }

    #     r = requests.get(url="https://www.spielemax.de/baby/", headers=headers)
    # # в параметры запроса пердаём url адрес
    #     if not os.path.exists("data"):      # если такой папке не существует, то сзададим ее
    #         os.mkdir("data")
    #
    #
    #     with open("data/page_spielzeug.html", "w", encoding="utf-8") as file:  # обязательно указать кодировочку при записи
    #         file.write(r.text)                   # получаем голый html без стилей

    with open("data/page_spielzeug.html") as file:  # читаем файл
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    pages_count = soup.find("div", class_="pages").find_all("a")[3].text  # забрать из предпоследней ссылки
    print(pages_count)  # получаем пятую страницу

    s = [int(s) for s in re.findall(r'-?\d+\.?\d*', pages_count)]  # извлекли число из того что мы вернули
    pages_count_num = int(''.join(map(str, s)))  # преобразвали число из списка в простое число

    # for i in range(1, pages_count_num + 1):
    #     url = f"https://www.spielemax.de/baby/?p={i}"
    #     print(url)
    #
    #     r = requests.get(url=url, headers=headers)
    #
    #     with open(f"data/page_{i}.html", "w", encoding="utf-8") as file:   # имя соответствует итерации
    #         file.write(r.text)
    #
    #     time.sleep(2)            # сохранили нужные нам страницы
    #
    # return pages_count_num + 1


# теперь нужно собрать нужную информацию

def collect_data():
    for page in range(1, 2):
        with open(f"data/page_{page}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find_all(class_="product-item")  # первый передаем тег, второй класс
        # print(items_cards)  # анализируем код, нужно вернуть название и цену

        for item in items_cards:
            name = item.find("a ", class_="product-item-link").text.strip()
            price_old = item.find("span", class_="price").text.lstrip("Euro. ")
            # price_new = item.find(id="product-price-339500").text.strip()
            product_url = item.find("a", {"class": "product-item-photo"}).get("href")

            # print(f"Article: {name} - Price: {price_old} - URL: {product_url}")


def main():
    collect_data()


if __name__ == '__main__':
    main()
