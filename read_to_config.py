import json
import logging


try:
    with open('config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        try:
            LOG_FILE = data['log_file']
        except KeyError:
            LOG_FILE = "jira_rating_check.log"
        finally:
            logging.basicConfig(
                filename=LOG_FILE,  # Имя файла для логов
                level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s',
                encoding='utf-8'
            )

        JIRA_URL = data['jira_url']
        USERNAME = data['username']
        PASSWORD_OR_TOKEN = data['password']
        SESSION = data['sessions']

        logging.info('Файл успешно прочитан')
        
except FileNotFoundError:
    raise("не обнаружен файл config.json")

except KeyError as key:
    logging.error(f"Не обнаржуен параметр {key}")



