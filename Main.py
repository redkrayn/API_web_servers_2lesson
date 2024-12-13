import os
import requests
import urllib.parse
from dotenv import load_dotenv


def shorten_link():
    url = 'https://api.vk.ru/method/utils.getShortLink'
    payload = {"access_token": token, "v": 5.81, "url": link}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    short_link = response.json()
    try:
        short_link.get("response").get("short_url")
    except:
        return "O_1"
    return short_link.get("response").get("short_url")


def count_clicks():
    urlparse = urllib.parse.urlparse(link).path.replace('/', '')
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    payload = {"access_token": token, "v": 5.81, "key": urlparse, "interval": "forever"}
    response = requests.get(url, params=payload)
    count_click = response.json()
    try:
        count_click.get("response").get("stats")[0]["views"]
    except:
        return "O_2"
    return count_click.get("response").get("stats")[0]["views"]


def is_shorten_link():
    if urllib.parse.urlparse(link).netloc == "vk.cc":
        return count_clicks()
    else:
        return shorten_link()


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("MY_TOKEN")
    link = input("Введите ссылку: ")
    if str(is_shorten_link()).isdigit():
        print("Количество переходов по ссылке:", is_shorten_link())
    elif str(is_shorten_link()) == "O_1":
        print("Неверный адресс")
    elif str(is_shorten_link()) == "O_2":
        print("По ссылке ещё не переходили")
    else:
        print("Короткая ссылка", is_shorten_link())




