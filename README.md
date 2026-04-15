# Anime Feeds

A modern anime news aggregator that automatically tracks releases from **Crunchyroll**, **My Anime List**, and **other** services via RSS.

The project consumes the RSS feed, processes the data, and displays the news in an organized and up-to-date manner.

Under active development — Discord bot support coming soon.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Feedparser](https://img.shields.io/badge/feedparser-6.x-orange)

---

## ✨ Current Features

- Automatic consumption of Feed RSS XML
- Intelligent post processing and normalization
- Generation of stable unique IDs (no collisions)
- Automatic background updates
- Responsive web interface with Jinja2
- Public JSON API (`/api/last/crunchyroll` and `/api/last/myanimelist`)
- Modular and scalable structure

---

## Technologies Used

- **Framework**: FastAPI
- **RSS Parser**: feedparser
- **Templating**: Jinja2
- **Validation**: Pydantic v2
- **In-memory caching**: Custom structure (`LinkedPosts` + `Node`)

---

## How to Execute the Project

### 1. Clone the repository

```bash
git clone https://github.com/olavob/anime-feeds.git

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

### 4. Run the application

```Bash
uvicorn app.main:app --reload --port 8000
```

Access: http://127.0.0.1:8000

## Project Structure

```
anime-feeds/
├── app/
│   ├── main.py                 # FastAPI configuration + lifespan
│   ├── Execeptions/            # Custom exceptions
│   ├── Services/
│   │   └── core.py             # Fetching and processing feeds
│   ├── Routers/                # Routes (home, api, feeds...)
│   ├── Schemas/                # Pydantic templates
│   ├── Templates/              # HTML + Jinja2
│   └── Static/                 # CSS, JS e assets
├── requirements.txt
└── README.md
```

## License

This project is under the MIT license.