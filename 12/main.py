import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_source_html(url):
    # driver = webdriver.Chrome(                # устаревший метод, не работает
    #     executable_path="C:\\Users\\Dennny\\Desktop\\PycharmProjects\\Scraping\\12\\chromedriver.exe"
    # )

    service = Service("C:\\Users\\Dennny\\Desktop\\PycharmProjects\\Scraping\\12\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()           # отсюда будем скролить страницу до определенного div

    try:
        driver.get(url=url)
        time.sleep(2)

        while True:
            find_more_element = driver.find_element(by=By.CLASS_NAME, value="catalog-list")    # скролить от

            if driver.find_elements(By.CLASS_NAME, 'hasmore-text'):     # скролить пока не дойдём до такого элемента
                with open("12/source-page.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)     # page_source позволяет сохранять контент
                break
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_more_element).perform()         # двигаемся и запускаем событие
                time.sleep(2)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url="https://spb.zoon.ru/medical/?search_query_form=1&m%5B5200e522a0f302f066000055%5D=1&center%5B%5D=50.28495905908034&center%5B%5D=29.47798285767327&zoom=4")


if __name__ == '__main__':
    main()


    # не закончил, пропал ориентир 'hasmore-text' , по которому завершается скролл