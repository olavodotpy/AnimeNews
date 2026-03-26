# Anime Feeds

A modern anime news aggregator that automatically tracks **Crunchyroll** releases via RSS.

The project consumes the official Crunchyroll feed, processes the data, and displays the news in an organized and up-to-date manner.

Under active development — soon with support for Anime News Network (ANN) and Discord Bot.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Feedparser](https://img.shields.io/badge/feedparser-6.x-orange)

---

## ✨ Current Features

- Automatic consumption of Crunchyroll RSS feeds and My anime list
- Intelligent post processing and normalization
- Generation of stable unique IDs (no collisions)
- Automatic background updates
- Responsive web interface with Jinja2
- Public JSON API (`/api/post/crunchyroll` and `/api/post/myanimelist`)
- Modular and scalable structure

---

## Technologies Used

- **Framework**: FastAPI
- **RSS Parser**: feedparser
- **Templating**: Jinja2
- **Validation**: Pydantic v2
- **In-memory caching**: Custom structure (`LinkedPosts` + `Node`)

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/olavodotpy/anime-feeds.git

cd anime-feeds

git checkout develop

python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
# venv\Scripts\activate
```

### 3. Install the dependencies

```Bash
pip install -r requirements.txt
```

### 4. Rode a aplicação

```Bash
uvicorn app.main:app --reload --port 8000
```

Access: http://127.0.0.1:8000

## Estrutura do Projeto

```
anime-feeds/
├── app/
│   ├── main.py                 # FastAPI configuration + lifespan
│   ├── Execeptions/            # Custom exceptions
│   ├── Services/
│   │   └── fetch.py            # Fetching and processing feeds
│   ├── Routers/                # Routes (home, api, feeds...)
│   ├── Schemas/                # Pydantic templates
│   ├── Templates/              # HTML + Jinja2
│   └── Static/                 # CSS, JS e assets
├── requirements.txt
└── README.md
```

## Licença

This project is under the MIT license.