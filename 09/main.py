import requests
from bs4 import BeautifulSoup
import datetime
import csv
import time
import json

start_time = time.time() # время запуска программы
def get_data():
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    # сохраним в файл, открываем фал на запись

    with open(f"labirint_{cur_time}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(                           # создаём обьект писателя и заголовки столбцов
            (
                "Название книги",
                "Автор",
                "Издательство",
                "Цена со скидкой",
                "Цена без скидки",
                "Процент скидки",
                "Наличие на складе"
            )
        )

    headers = {
        "accept": "* / *",           # обязательное поле
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    url = "https://www.labirint.ru/genres/153/?display=table"

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    pages_count = int(soup.find("div", class_="pagination-number").find_all("a")[-1].text) # собираем все ссылки которые содержатся, и забираем последнюю


    for page in range(1, pages_count + 1):
    # for page in range(1, 2):
        url = "https://www.labirint.ru/genres/153/?display=table&page={page}"

        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        books_items = soup.find("tbody", class_="products-table__body").find_all("tr")

        books_data = []            # создадим список под собранные данные
        for item in books_items:
           book_data = item.find_all("td")
           try:
               # book_title = book_data[0].find("a").text.strip()
               book_title = book_data[0].find_all("a")
               book_title = ":" .join([ba.text for ba in book_title])    # непонятно
           except:
               book_title = "Нет названия книги"
           try:
               book_author = book_data[1].text.strip()
           except:
               book_author = "Нет автора"
           try:
               book_publishing = book_data[2].text.strip()
           except:
               book_publishing = "Нет издательства"
           try:
               book_new_price = int(book_data[3].find("div", class_="price").find("span").find("span").text.strip().replace(" ", ""))        # получим цену со скидкой
               # метод replace для того чтобы удалить пробел между цифрами,
           except:
               book_new_price = "Нет нового прайса"
           # аналогично забираем прайс без скидки
           try:
               book_old_price = int(book_data[3].find("span", class_="price-old").text.strip().replace(" ", ""))
           except:
               book_old_price = "Нет старой цены"
           try:
               book_sale = round(((book_old_price - book_new_price) / book_old_price) * 100)      # формула скидки из гугла
           except:
               book_sale = "Нет скидки"
           try:
               book_status = book_data[-1].text.strip()
           except:
               book_status = "Нет статуса"
           # print(book_title)
           # print(book_author)
           # print(book_publishing)
           # print("#" * 20)
           # print(book_new_price)
           # print(book_old_price)
           # print(book_sale)

           # наполняем список на каждой итерации


           books_data.append(
               {
                   "book_title": book_title,
                   "book_author": book_author,
                   "book_publishing": book_publishing,
                   "book_new_price": book_new_price,
                   "book_old_price": book_old_price,
                   "book_sale": book_sale,
                   "book_status": book_status
               }
           )
           with open(f"labirint_{cur_time}.csv", "a") as file:          # дописываем строки
               writer = csv.writer(file)

               writer.writerow(
                   (
                       book_title,
                       book_author,
                       book_publishing,
                       book_new_price,
                       book_old_price,
                       book_sale,
                       book_status
                   )
               )

        print(f"Обработана {page}/{pages_count}")    # промежуточный результат работы
        time.sleep(1)

        with open(f"labirint_{cur_time}.json", "w") as file:
            json.dump(books_data, file, indent=4, ensure_ascii=False)
def main():
    get_data()
    finish_time = time.time() - start_time        # отнимем время от текущего
    print(finish_time)




if __name__ == '__main__':
    main()

# иероглифы откорректировать через Google_ таблицы...