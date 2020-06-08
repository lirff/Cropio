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

response = requests.post('https://cropio.com/api/v3/sign_in', data=values, headers=headers)
print('Статус код: ', response.status_code)
# преобразовываем json  в словарь
json = response.json()
print('Ответ в списке, json раскодировали выше: ', json)
user_api_token = json.get('user_api_token')
print('Достали токен: ', user_api_token)
# добавляем с headers токен
headers['X-User-Api-Token'] = user_api_token
print(headers)
