from read_to_config import *
import requests
from requests.auth import HTTPBasicAuth


response = requests.get(
    url=JIRA_URL,
    auth=HTTPBasicAuth(USERNAME, PASSWORD_OR_TOKEN)
)
