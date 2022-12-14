# собрать данные из интернета и сложить их аккуратно в JSON
import requests
from bs4 import BeautifulSoup
import lxml
import json

# первым делом нужно собрать все ссылки

# создадим список под наши ссылки

fests_urls_list = []

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

for i in range(0, 24, 24):  # количество запросов для сбора всех ссылок
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=8%20Dec%202022&to_date=29%20Jun%202025&maxprice=500&o={i}&bannertitle=May"
    print(url)  # отображаем наши ссылки
    # конкретно выше мы взяли шаг оффсетов, и проитерировали так чтобы получить 8 ссылок с нужными нам страницами

    req = requests.get(url=url, headers=headers)  # собственно сам запрос вложенный в переменную
    json_data = json.loads(req.text)  # передаём результат выполнения запроса
    # данные содержатся в html коде с одноименным ключом
    html_response = json_data["html"]

    with open(f"data/index_{i}.html", "w",
              encoding="utf-8") as file:  # соскряпали в папочку наши данные, открыли файл на запись
        file.write(html_response)

    with open(f"data/index_{i}.html") as file:
        src = file.read()

    # ищем способ собрать ссылки
    # зацепились за общий класс class="card-details-link"

    soup = BeautifulSoup(src, "lxml")  # создаём экземпляр класса и передаем в качестве аргумента наш код и парсер lxml
    cards = soup.find_all("a", class_="card-details-link")  # найдём все теги с классом ""

    for item in cards:  # пробежимся по ним, и заберем теги
        fest_url = "https://www.skiddle.com" + item.get("href")
        fests_urls_list.append(fest_url)  # на каждой итерации, добавляем тег в список
# теперь у нас есть ссылки, добавляем к ним домен для полной работоспособности
print(fests_urls_list)

# теперь напишем код для перехода по каждой ссылке и сбору информации


for url in fests_urls_list:  # перебираем наш список с ссылками
    print(url)

    req = requests.get(url=url, headers=headers)  # отправляем запрос

    try:
        soup = BeautifulSoup(req.text, "lxml")               # извлекаем из запроса текстовый файл
        fest_info_block = soup.find("div", class_="css-oh7gsz")  # забрали блок
        fest_name = fest_info_block.find("h2").text.strip()  # забрали из блока по тегу имя и обрежем стрипом пробелы
        fest_date = fest_info_block.find("h3").text.strip()  # получим также дату фестиваля

        print(fest_name)
        print(fest_date)
        print("#" * 20)
    except Exception as ex:
        print(ex)
        print("Damn ...There some error...")
