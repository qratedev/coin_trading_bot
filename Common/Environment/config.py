# /Common/Environment/config.py
import configparser

filename = 'config.ini'
_ini = configparser.ConfigParser()
_ini.read(filename)

# Binance
api_key = _ini['Binance']['api_key']
secret_key = _ini['Binance']['secret_key']

# Telegram
telegram_token = _ini['Telegram']['telegram_token']
chat_id = _ini['Telegram']['chat_id']


def set_Value(section, key, value):
    _ini.set(section, key, value)
    cfgfile = open(filename, 'w')
    _ini.write(cfgfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
    cfgfile.close()
