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
    return short_link.get("response").get("short_url")


def count_clicks():
    urlparse = urllib.parse.urlparse(link).path.replace('/', '')
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    payload = {"access_token": token, "v": 5.81, "key": urlparse, "interval": "forever"}
    response = requests.get(url, params=payload)
    count_click = response.json()
    return count_click.get("response").get("stats")[0]["views"]


def is_shorten_link():
    urlparse = urllib.parse.urlparse(link).path.replace('/', '')
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    payload = {"access_token": token, "v": 5.81, "key": urlparse, "interval": "forever"}
    response = requests.get(url, params=payload)
    get_error = response.json()
    if urllib.parse.urlparse(link).netloc == "vk.cc":
        if get_error.get('error'):
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["TOKEN_VK_API"]
    link = input("Введите ссылку: ")
    if is_shorten_link() == False:
        try:
            shorten_link()
            print("Короткая ссылка", shorten_link())
        except AttributeError:
            print("Неверный адресс")
    else:
        try:
            count_clicks()
            print("Количество переходов по ссылке:", count_clicks())
        except IndexError:
            print("По ссылке ещё не переходили")






