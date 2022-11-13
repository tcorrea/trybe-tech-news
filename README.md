<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto no qual você pode customizar e reutilizar todas as vezes que for executar o trybe-publisher.

Para deixá-lo com a sua cara, basta alterar o seguinte arquivo da sua máquina: ~/.student-repo-publisher/custom/_NEW_README.md

É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você;
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->

![TRYBE_TECH_NEWS](https://user-images.githubusercontent.com/20843662/201528891-ae8c5cc2-7747-4ba3-9f01-619488a362c7.png)

![GitHub top language](https://img.shields.io/github/languages/top/tcorrea/trybe-tech-news)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat-square&logo=linkedin&logoColor=white&color=ffb86c)](https://www.linkedin.com/in/thiago-de-carvalho-correa/)

# Descrição

Projeto desenvolvido no módulo de ciência da computação na instituição [Trybe](https://www.betrybe.com/), com o objetivo de raspar dados (_scraper_) de uma [página](https://blog.betrybe.com) usando python e inserir no banco de dados (_mongodb_).

# Estrutura do projeto

Estrutura do projeto e descrição dos arquivos que foram desenvolvidos por mim e pela Trybe.

```
Legenda:
🔸Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹Arquivos desenvolvidos por mim.
.
├── tech_news
│   ├── analyzer
│   │   ├── 🔹ratings.py
│   │   └── 🔹search_engine.py
│   ├── 🔸database.py
│   └── 🔹menu.py
│   └── 🔹scraper.py
├── tests
│   ├── 🔸assets/*
│   ├── 🔸__init__.py
│   ├── 🔸generate_fixture.py
│   ├── 🔸news.py
│   ├── 🔸test_menu.py
│   ├── 🔸test_ratings.py
│   ├── 🔸test_scraper.py
│   ├── 🔸test_search_engine.py
│   └── 🔸utils.py
├── 🔸dev-requirements.txt
├── 🔸docker-compose.yml
├── 🔸Dockerfile
├── 🔸pyproject.toml
├── 🔸README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
├── 🔸setup.py
└── 🔸trybe.yml
```

# Instalação

1. Clone o repositório

-   Use o comando:
    ```
    git clone https://github.com/tcorrea/trybe-tech-news
    ```
-   Entre na pasta do repositório que você acabou de clonar:
    ```
    cd trybe-tech-news
    ```

2. Crie o ambiente virtual para o projeto

    ```
    python3 -m venv .venv && source .venv/bin/activate
    ```

3. Instale as dependências
    ```
    python3 -m pip install -r dev-requirements.txt
    ```
4. Rodando MongoDB via Docker
    ```
    docker-compose up -d mongodb
    ```

# Como usar

1. Para inserir e listar uma quantidade de notícias.

-   Use o comando:
    ```
    python3 -i tech_news/scraper.py
    ```
-   Depois:
    ```
    get_tech_news(quantidade_de_news)
    ```
-   Retorno:
    ```python
    >>> get_tech_news(1)
    [
        {
            "url":"https://blog.betrybe.com/tecnologia/informatica-basica/",
            "title":"Informática básica: o que é e quais os 16 conceitos principais",
            "timestamp":"09/11/2022",
            "writer":"Lucas Custódio",
            "comments_count":0,
            "summary":"Os computadores dominaram o mundo. Por isso, é uma grande vantagem ter algum conhecimento em Informática básica, especialmente se você for da área de tecnologia.",
            "tags":[
                ],
                "category":"Tecnologia"
        }
    ]
    ```

2. Pesquisar notícias por título.

-   Use o comando:
    ```
    python3 -i tech_news/analyzer/search_engine.py
    ```
-   Depois:
    ```
    search_by_title("Informática")
    ```
-   Retorno - Uma lista com o título e o link para a notícia:
    ```python
    [('Informática básica: o que é e quais os 16 conceitos principais', 'https://blog.betrybe.com/tecnologia/informatica-basica/')]
    ```

3. Pesquisar notícias por data.

-   Use o comando:
    ```
    python3 -i tech_news/analyzer/search_engine.py
    ```
-   Depois:
    ```
    search_by_date("2022-11-09")
    ```
-   Retorno - Uma lista com o título e o link para a notícia:
    ```python
    [('Informática básica: o que é e quais os 16 conceitos principais', 'https://blog.betrybe.com/tecnologia/informatica-basica/')]
    ```
