from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(single_news["title"], single_news["url"]) for single_news in news]


# Requisito 7
def search_by_date(date):
    try:
        # strptime compara a data recebida com "%Y-%m-%d" e depois converte
        # para o formato que esta no banco de dados
        formated_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    news = search_news({"timestamp": formated_date})
    return [(single_news["title"], single_news["url"]) for single_news in news]


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(single_news["title"], single_news["url"]) for single_news in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
