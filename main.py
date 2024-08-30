import requests
import json
from key import KEY

url =f"https://api.unsplash.com/photos/random?client_id={KEY}"

response = requests.request("GET", url)

if response.ok:
    arr=response.json()

    if arr['description']==None:
        if arr['alt_description']==None:
            print("Описание отсутствует")
        else:
            print(f"Описание: {arr['alt_description']}")
    else:
        print(f"Описание: {arr['description']}")

    print(f"Число просмотров: {arr['views']}")
    print(f"Число лайков: {arr['likes']}")
    print(f"Дата создания: {arr['created_at']}")
    print(f"Дата публикации: {arr['updated_at']}")
else:
    print("Не удалось получить ответ")