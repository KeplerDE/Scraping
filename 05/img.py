import requests
import img2pdf

# первая часть задания - скопировать изображения с сайта
def get_data():         # нам нужно пробежаться по 48ми ссылкам и сохранить изображение
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    # img_list = []      # создадим список для доюавления фоточек
    # for i in range(1, 49):
    #     url = f"https://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"    # на каждой итерации будем менять число фотки
    #     req = requests.get(url=url, headers=headers)      # отправляем запрос и подкладываем наши заголовки
    #     response = req.content               # сохраняем ответ
    #
    #     with open(f"media/{i}.jpg", "wb") as file:    # записываем изображения в папку
    #         file.write(response)
    #         img_list.append(f"media/{i}.jpg")      # уложили фотки в список
    #         print(f"Downloaded {i} of 48")
    #
    # print("#" * 25)
    # print(img_list)
    # # вторая часть задания - сложить эти файлы в pdf файл, для этого используем спец. библиотеку
    #

    # создаём pdf файл
    # with open("result.pdf", "wb") as f:
    #     f.write(img2pdf.convert(img_list))          # вызываем метод и передаём список изображений
    #
    # print("PDF file created successfully!")
def write_to_pdf():
    # print(os.listdir("media"))
    img_list = [f"media/{i}.jpg" for i in range(1, 49)]

    # create PDF file
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully!")
def main():
    get_data()
    # write_to_pdf()


if __name__ == '__main__':
    main()