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
    'Content-Type': 'application/json',
    'X-User-Api-Token': 'PYTyn6uVy5nRUpS3dqwN'
}

fields = requests.get(url=url.format('fields/25000'), headers=headers)
#print(fields.json())
o = fields.json()
print(o['data'])
k = o['data']
j = k['name']
print('Номер поля: ', j)
