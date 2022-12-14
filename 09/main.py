import requests
from bs4 import BeautifulSoup


def get_data():
    headers = {
        "accept": "* / *",           # обязательное поле
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    url = "https://www.labirint.ru/genres/153/?display=table"

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    pages_count = int(soup.find("div", class_="pagination-number").find_all("a")[-1].text) # собираем все ссылки которые содержатся, и забираем последнюю


    # for page in range(1, pages_count + 1):
    for page in range(1, 2):
        url = "https://www.labirint.ru/genres/153/?display=table&page={page}"

        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        books_items = soup.find("tbody", class_="products-table__body").find_all("tr")


        for item in books_items:
            book_data = item.find_all("td")

            try:
                book_title = book_data[0].find("a").text.strip()

            except:
                book_title = "Нет названия книги"

            try:
                book_author = book_data[1].text.strip()
            except:
                book_author = "Нет автора"

            print(book_title)
            print(book_author)
            print("#" * 20)








def main():
    get_data()



if __name__ == '__main__':
    main()

