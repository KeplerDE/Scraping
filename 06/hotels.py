import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time



def get_data(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }
# # заголовки обязательная часть, т.к. не получится соскряпить
#     r = requests.get(url=url, headers=headers)
#
#     with open("index.html", "w", encoding="utf-8") as file:        # сохраняем страницу как такст
#         file.write(r.text)            # по факту мы собрали хрень, ищем норммальную ссыылку с данными
# дубль 2, нашли правильную ссылку, отправляем запрос

    r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&hotel_link=/hotel/id/%HOTEL_ID%", headers=headers)
    print(r.text)
    soup = BeautifulSoup(r.text, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")     # отели обернуты в карточки

    for hotel_url in hotels_cards:
        hotel_url = hotel_url.find("a").get("href")          # пройдёмся, и заберем типа ссылки на отели
        print(hotel_url)

# второй способ сбора данных через селениум
def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")


    try:
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Dennny\\PycharmProjects\\Scraping\\06\\chromedriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        with open("index_selenium.html", "w") as file:
            file.write(driver.page_source)

    except Exception as ex:                  # проверяем данные на ошибки
        print(ex)
    finally:                                 #  завершает работу нашего драйвера
        driver.close()
        driver.quit()

def main():
    # get_data("https://www.tury.ru/hotel/most_luxe.php")
    get_data_with_selenium("https://www.tury.ru/hotel/most_luxe.php")


if __name__ == '__main__':
    main()



    # DeprecationWarning: executable_path has been deprecated, please pass in a Service object
    #   driver = webdriver.Chrome    --------- доделать этот момент