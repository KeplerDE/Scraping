import requests
from bs4 import BeautifulSoup
import json  # импортируем чтобы сохранить данные в этот формат

from unicodedata import category

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    "accept": "*/*",  # юзер агент и accept, показываем сайту что мы не бот
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
# req = requests.get(url, headers=headers)        # первым обязательным параметром передаётся ссылка, вторым необязательным заголовки
# src = req.text          # сохраняем обьект, применяем метод текст, выводим
# # print(src)             # выводим получаенный код страницы
#

# сохраним теперь нашу страницу в файл

# with open("index.html", "w", encoding="utf-8") as file:         #  сохраним это в файл, в избежании бана из за многочисленных запросов
#     file.write(src)                                             # добавляем кодировочку для чёткого вывождения и посмотрим в .html
#
#
#
#


with open("index.html", encoding="utf-8") as file:  # открываем наш файл в режиме чтения
    src = file.read()

soup = BeautifulSoup(src, "lxml")  # создали экзмепляр класса и в качестве параметра передаём класс ссылок всех

#
# all_categories_dict = {}         # добавим данные в словарь, и на каждой итерации цикла будем добавлять данные в словарь
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
# for item in all_products_hrefs:                                     # получаем все ссылки из нашей страницы
#     item_text = item.text               # создали переменную и применяем к ней метод для извлечения текста
#     item_href = "https://health-diet.ru" + item.get("href")
#     print(f"{item_text}: {item_href}")              # отображаем структуированно наш текст и ссылку
#     all_categories_dict[item_text] = item_href     # ключом является текст, значением ссылка
#
# print(all_categories_dict) #
#
# with open("all_categories_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)  # параметр индент это отступ в нашем файле, ensure помогает с кодировкой


with open("all_categories_dict.json", encoding="utf-8") as file:
    all_categories = json.load(file)  # загружаем файл в переменную
#
#
#
# print(all_categories)              # находится полученный словарь


count = 0
for category_name, category_href in all_categories.items():  # выбираем две категории

    if count == 0:
        rep = [",", " ", "-", "'"]
        for item in rep:
            if item in category_name:  # заменяем в категории символы, на другой
                category_name = category_name.replace(item, "_")
                print(category_name)

            req = requests.get(url=category_href, headers=headers)  # переходим к выборке категорий на сайте
            src = req.text

            with open(f"data/{count}_{category_name}.html", "w",
                      encoding="utf-8") as file:  # сохраним нашу страницу под именем категорий
                file.write(src)

            count += 1
