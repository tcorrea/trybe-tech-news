import requests as rq
from parsel import Selector
import time


# Requisito 1
def fetch(url, timeout=3):

    try:
        response = rq.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=timeout
        )
        time.sleep(1)
    except (rq.ReadTimeout, rq.HTTPError):
        return None

    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    return Selector(html_content).css(".cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    return Selector(html_content).css(".next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
