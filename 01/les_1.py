# This Python file uses the following encoding: utf-8

from bs4 import BeautifulSoup                               # импортируем библиотек для анализа



with open("index.html", encoding="utf-8") as file:
    src = file.read()                                 #  в переменную вкладываем наш html файл
#print(src)


soup = BeautifulSoup(src, "lxml")                     # создаём переменную и вкладываем в нее экземпляр класса с параметрами src & lxml


# получается мы создали обьект к которому можем обращаться и применять методы

title = soup.title   # применили метод и вывели title
print(title)

# print(title.text)
# print(title.string)
# .find, .find_all,

#page_h1 = soup.find("h1")   # нашли и вывели заголовок
#print(page_h1)


#page_all_h1 = soup.find_all("h1")  # обернули заголовок в список, который далее например мы можем перебрать
#print(page_all_h1)


#for item in page_all_h1:
    #print(item.text)


#user_name = soup.find("div", class_="user__name")    # указываем div чтобы конкретно спарсить, то что нужно
#print(user_name)                           # получаем из метода супа
#print(user_name.text)                      # а так мы получаем то что лежит внутри
#print(user_name.text.strip())              # так тоже получаем чистый текст


#user_name = soup.find("div", {"class": "user__name"}). find("span").text  # заглянули внутрь и забрали span
#print(user_name)




find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")


#print(find_all_spans_in_user_info)

#print(find_all_spans_in_user_info[0])            # по индексу
#print(find_all_spans_in_user_info[2].text)      # вывести чистый текст



social_links = soup.find(class_="social__networks").find(            # нужно спарсить ссылки
    "ul").find_all("a")
print(social_links)





