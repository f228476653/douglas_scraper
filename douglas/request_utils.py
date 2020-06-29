from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

ua = UserAgent(verify_ssl=False)
def bs(content):
    return BeautifulSoup(content, "html.parser")

def requests_get(url):
    headers = {
        "User-Agent": str(ua.random)
    }
    return requests.get(url=url, headers=headers)