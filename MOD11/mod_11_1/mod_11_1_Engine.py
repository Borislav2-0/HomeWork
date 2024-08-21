import requests
from PIL import Image


class Photoshoper:

    def __init__(self):
        self.url = input('Введите URL-адрес, чтобы скачать изображение: ')
        self.img = 'image.png'

    def downloading(self):
        response = requests.get(self.url)
        res_status_code = response.status_code
        if response.ok:
            print(f'Статус код по указанному URL: {res_status_code}')
        with open(self.img, 'wb') as file:
            file.write(response.content)

    def photoshop(self):
        SOURCE_DIR = './'
        photo = Image.open(SOURCE_DIR + self.img)
        new_size = input('Введите размеры фото (например, 325, 325): ')
        t = tuple(int(item) for item in new_size.split(','))
        profile_picture = photo.crop((0, 0, photo.width, photo.width)).resize(t)
        profile_picture = profile_picture.convert('L')
        save_photo = input('Введите имя и расширение изображения для его сохранения (пример: <имя.расширение>): ')
        profile_picture.save(SOURCE_DIR + save_photo)

        print(profile_picture.size)
        print(profile_picture.mode)
        print(profile_picture.format)
        print(profile_picture.info)

        profile_picture.show()


ph = Photoshoper()
ph.downloading()
ph.photoshop()
