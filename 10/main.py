import requests
from bs4 import BeautifulSoup
import time


def test_request(url, retry=5):  # количество попыток
    headers = {
        "accept": "text/html, */*; q=0.01",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url=url, headers=headers)
        print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        time.sleep(3)
        if retry:
            print(f"[INFO] retry={retry} => {url}")
            return test_request(url, retry=(retry - 1))
        else:
            raise
    else:
        return response
    # url = "https://www.labirint.ru/books/813550/"
    # print(f"[INFO]{url} ")


def main():
    with open("books_urls.txt") as file:
        books_urls = file.read().splitlines()      # (важный метод) разбивает строку на множество строк, возвращая их списком

    for book_url in books_urls:
        # test_request(url=book_url)

        try:
            r = test_request(url=book_url)
            soup = BeautifulSoup(r.text, "lxml")
            print(f"{soup.title.text}\n{'-' * 20}")
        except Exception as ex:          # при неудачной попытке, мы переходим к следующей итерации
            continue

if __name__ == "__main__":
    main()
