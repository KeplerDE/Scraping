from selenium import webdriver
import time
driver = webdriver.Chrome("C:\\Users\\Dennny\\Desktop\\PycharmProjects\\Scraping\\12\\chromedriver.exe")
driver.get("https://spb.zoon.ru/medical/?search_query_form=1&m%5B5200e522a0f302f066000055%5D=1&center%5B%5D=50.28495905908034&center%5B%5D=29.47798285767327&zoom=4")

time.sleep(3)
driver.close()