from read_to_config import *
import requests
from requests.auth import HTTPBasicAuth

headers = {
        "Authorization": f"Bearer {PASSWORD_OR_TOKEN}", # Токен передается как Bearer
        "Accept": "application/json"
        }

try:
    response = requests.request("GET", JIRA_URL, headers=headers)
    print(response.status_code)
    logging.info("Подключение успешно")
except:
    logging.error("Ошибка подключения")

with open('test.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
