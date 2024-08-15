from PIL import Image, ImageChops

SOURCE_DIR = './'
p1 = Image.open(SOURCE_DIR + 'image1.png')

# получение информации об изображении
print(p1.size)
print(p1.mode)
print(p1.format)
print(p1.info)

# обрезка фото и сохранение в другом формате
profile_picture = p1.crop((0, 0, p1.width, p1.width)).resize((745, 745))

profile_picture.save(SOURCE_DIR + 'Aleksandr_III.jpeg')

# просмотр изображения
profile_picture.show()
