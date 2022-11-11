from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()
    # usando a função sort() do mongo
    # sorted_news = (
    #     get_collection().find({})
    #     .sort([("comments_count", -1), ("title", 1)])
    # )
    sorted_news = sorted(
        news,
        # função que organiza pelo comments_count e depois por title se tiver
        # a mesma quantidade de comments_count
        key=lambda item: (item["comments_count"], item["title"]),
        reverse=True,
    )
    return [
        (single_news["title"], single_news["url"])
        for single_news in sorted_news[:5]
    ]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = [single_news["category"] for single_news in news]
    # categories_occurrences:list[tuple]
    categories_occurrences = Counter(categories).most_common(5)
    sorted_categories = sorted(
        categories_occurrences,
        # -item[1] organiza por qtd de ocorrencia: recebi ajuda -item[1]
        # item[0] onder alfabetica
        key=lambda item: (-item[1], item[0]),
    )
    return [category[0] for category in sorted_categories]
