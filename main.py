# main.py
from Common.Environment import config

if __name__ == '__main__':
    print(f'key: {config.api_key} | secret_key: {config.secret_key}')
