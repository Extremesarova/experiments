import requests
import json

client_id = '2cc0611b0f9e25ea9d98'
client_secret = '65c7be0f945633b8302dc4872ec3d38f'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

art_people = {}
with open("python/3.5.2_input.txt", "r") as f:
    for input in f:
        # инициируем запрос с заголовком
        r = requests.get(f"https://api.artsy.net/api/artists/{input.strip()}", headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        if 'sortable_name' in j:
            art_people[j['sortable_name']] = int(j['birthday'])
            # print(j['sortable_name'])

sorted_art = dict(sorted(art_people.items(), key=lambda item: (item[1], item[0])))

for key in sorted_art:
    print(key)