import datetime
import json
import requests


headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_data():
    # start_time = datetime.datetime.now()

    url = "https://roscarservis.ru/catalog/legkovye/?set_filter=Y&sort%5Brecommendations%5D=asc&PAGEN_1=2"
    r = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(r.text)
    #
    # print(r.json())
    #
    # with open("r.json", "w") as file:
    #     json.dump(r.json(), file, indent=4, ensure_ascii=False)


# проблема со страничками, нет пагинации, а значит не выплывает JSON со всеми данными




def main():
    get_data()


if __name__ == '__main__':
    main()