import requests
import json
import logging


try:
    with open('config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        LOG_FILE = data['log_file']
        logging.basicConfig(
            filename=LOG_FILE,  # Имя файла для логов
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            encoding='utf-8'
        )

        JIRA_URL = data['jira_url']
        USERNAME = data['username']
        PASSWORD_OR_TOKEN = data['password']

        logging.info('Файл усмешно прочитан')
        
except FileNotFoundError:
    raise("не обнаружен файл config.json")

except KeyError as key:
    logging.error(f"Не обнаржуен параметр {key}")

