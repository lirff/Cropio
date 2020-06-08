import requests

url = 'https://cropio.com/api/v3/{}'
login = 'agro@kzpgroup.ru'
pwd = '123456'

values = """
  {
    "user_login": {
      "email": "agro@kzpgroup.ru",
      "password": "123456"
    }
  }
"""

headers = {
    'Content-Type': 'application/json'
}

r = requests.post('https://cropio.com/api/v3/sign_in', data=values, headers=headers)


print('Статус код: ', r.status_code)
print('Вывод в тип данных: ', r.content, type(r.content), sep='\r\n')

t = r.json()
print('Принт тип t и разделяем : ', t, type(t), sep='\r\n')

token = t.get('user_api_token')
print('Получив токен, выводим его: ', token)
print('Выводим заголовок: ', headers)
headers['X-User-Api-Token'] = token
print('Добавили в заголовок user_id_token: ', headers)


fields = requests.get(url=url.format('fields/36307'), headers=headers)
print('Выводим field.headers: ', fields.headers)
print('Выводим fields.content: ', fields.content)
print('Выводим fields.json: ', fields.json())

data = fields.json().get('data')

print('Вывод data: ', data)
