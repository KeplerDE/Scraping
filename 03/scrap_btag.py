import requests
from bs4 import BeautifulSoup
import json

# persons_url_list = []
#
#
# for i in range(0, 740, 20):           # цикл с перебором ссылок по 20 морд
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
#     # print(url)
#     q = requests.get(url)            # запихали в переменную запрос
#     result = q.content               # наш запрос плюс  (контент из кода html)
#
#     soup = BeautifulSoup(result, 'lxml')                # переменная (передаём параметром первым , и типа парсера)
#     persons = soup.find_all('a')  # ищем по классу наших людей
#
#     for person in persons:          # то что переберем засунем в список
#         person_page_url = person.get("href")
#         persons_url_list.append(person_page_url)
#
# with open('persons_url_list.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')

with open('persons_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name': person_name,
            'company_name': person_company,
            'social_networks': social_networks_urls
        }
        count += 1
        print(f'#{count}: {line} is done!')

        data_dict.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)




