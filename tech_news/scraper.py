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
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    # TODO: pegar comentarios
    # comments_count = selector.css()
    summary = selector.css("p::text").get()
    tags = selector.css(".menu-item-object-post_tag a::text").getall()
    tags_ = list(set(tags))
    category = selector.css(
        ".meta-category .category-style .label::text"
    ).get()
    print("\n timestamp", url)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
