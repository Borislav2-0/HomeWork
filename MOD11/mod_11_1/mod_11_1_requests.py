import requests
import pprint

# Запрос и проверка статус-кода
response = requests.get('https://httpbin.org/#/')

res_status_code = response.status_code
if response.ok:
    print(f'Статус код по указанному URL: {res_status_code}')

# передача параметров
search_query = {'query': 'python'}
response_1 = requests.get('https://httpbin.org/get', params=search_query)

res_json = response_1.json()
pprint.pprint(res_json)

# передача cookie
cookie = {'session_token': '123456789'}

response_2 = requests.get('https://httpbin.org/cookies', cookies=cookie)
print(response_2.text)

# сохранение изображения
IMG_URL = 'https://sun9-79.userapi.com/impg/wezykawsa41k6lFsBp39DoN1m1byGt0OGN40-w/Vhx9YIu7RZs.jpg?size=745x1024&quality=95&sign=d5260dfb88cffe51ccc394528eba5f05&c_uniq_tag=ef0_D5kcj36qiC3q0RtBVrcfc54LSxJLBlcMLDAn16M&type=album'

response_3 = requests.get(IMG_URL)

with open('image1.png', 'wb') as file:
    file.write(response_3.content)
