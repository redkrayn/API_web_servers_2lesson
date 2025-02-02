import os
import requests
import urllib.parse
from dotenv import load_dotenv


def shorten_link(token, link):
    url = 'https://api.vk.ru/method/utils.getShortLink'
    payload = {"access_token": token, "v": 5.81, "url": link}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    short_link = response.json()
    return short_link.get("response").get("short_url")


def count_clicks(token, link):
    url_path = urllib.parse.urlparse(link).path.replace('/', '')
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    payload = {"access_token": token, "v": 5.81, "key": url_path, "interval": "forever"}
    response = requests.get(url, params=payload)
    count_click = response.json()
    return count_click.get("response").get("stats")[0]["views"]


def is_shorten_link(token, link):
    url_path = urllib.parse.urlparse(link).path.replace('/', '')
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    payload = {"access_token": token, "v": 5.81, "key": url_path, "interval": "forever"}
    response = requests.get(url, params=payload)
    mistake = response.json()
    return mistake.get('error')


def main():
    load_dotenv()
    token = os.environ["VK_API_TOKEN"]
    link = input("Введите ссылку: ")
    if is_shorten_link(token, link):
        try:
            print("Короткая ссылка", shorten_link(token, link))
        except AttributeError:
            print("Неверный адресс")
    else:
        try:
            print("Количество переходов по ссылке:", count_clicks(token, link))
        except IndexError:
            print("По ссылке ещё не переходили")


if __name__ == "__main__":
    main()







