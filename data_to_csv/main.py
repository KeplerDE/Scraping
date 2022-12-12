import csv

name_1 = "Alex"
name_2 = "Alexa"

# with open("data.csv", "w", ) as file:  # запись в такой формат
#     writer = csv.writer(file)
#     writer.writerow(  # обьединяет метод в список
#         # [name_1, name_2]
#         ("user_name", "user_address")
#     )
#
users_data = [
    ["user_1", "address1"],
    ["user_2", "address2"],
    ["user_3", "address3"],
]
#
# for user in users_data:
#     with open("data.csv", "a", ) as file:            # аргумент "a"    для полной записи
#         writer = csv.writer(file)
#         writer.writerow(
#             user
#         )


# можно без перебора записать сразу файл, одним куском кода

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(
        users_data
    )



