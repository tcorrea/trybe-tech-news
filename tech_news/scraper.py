import requests as rq
from parsel import Selector
import time

# FIX: arrumar import do modulo database
from tech_news.database import create_news, find_news


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
    summary = "".join(
        selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()

    return {
        # https://stackoverflow.com/questions/52849274/getting-the-current-url-page-ref-scrapy
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "summary": summary,
        "tags": selector.css(".post-tags li a::text").getall(),
        "category": selector.css(
            ".meta-category .category-style .label::text"
        ).get(),
    }


# Requisito 5
# def get_tech_news(amount, url="https://blog.betrybe.com/", news_links=[]):
def get_tech_news(amount):
    # if len(news_links) >= 0 and len(news_links) < amount:
    #     content = fetch(url)
    #     next_page_link = scrape_next_page_link(content)
    #     news_links.extend(scrape_novidades(content))
    #     return get_tech_news(amount, next_page_link, news_links)

    main_page = fetch("https://blog.betrybe.com/")
    next_page_link = scrape_next_page_link(main_page)

    news_links: list = scrape_novidades(main_page)

    while len(news_links) < amount:
        next_page_content = fetch(next_page_link)
        next_page_link = scrape_next_page_link(next_page_content)
        news_links.extend(scrape_novidades(next_page_content))

    news = [
        # scraping cada news recebida
        scrape_noticia(
            # fetch cada link retornando um html para scrap_noticia
            fetch(single_news)
        )
        for single_news in news_links[:amount]
    ]
    create_news(news)
    return news
