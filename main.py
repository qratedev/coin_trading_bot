
from Common.Environment import config
import requests


def send_message(message):
    url = f"https://api.telegram.org/bot{config.telegram_token}/sendMessage?chat_id={config.chat_id}&text={message}"
    print(requests.get(url).json())  # this sends the message


if __name__ == '__main__':
    # print(f'key: {config.api_key} | secret_key: {config.secret_key} | telegram_token: {config.telegram_token}')
    send_message('테스트')



