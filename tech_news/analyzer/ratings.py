from tech_news.database import find_news


# Requisito 10
def top_5_news():
    top_5 = find_news()
    sorted_news = sorted(
        top_5,
        # função que organiza pelo comments_count e depois por title se tiver
        # a mesma quantidade de comments_count
        key=lambda item: (item["comments_count"], item["title"]),
        reverse=True,
    )
    result = [
        (single_news["title"], single_news["url"])
        for single_news in sorted_news[:5]
    ]
    print("\nSORTED VAR:", result)
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
