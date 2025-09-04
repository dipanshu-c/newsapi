from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # ✅ load environment variables

app = Flask(__name__)

# ✅ Define categories globally
ALL_CATEGORIES = ["General", "Business", "Entertainment", "Health", "Science", "Sports", "Technology"]

# ✅ Helper function to fetch news
def fetch_news(url):
    try:
        r = requests.get(url).json()
        return r.get('articles', [])
    except Exception as e:
        print("Error fetching news:", e)
        return []


@app.route("/")
def home():
    url = f"{os.getenv('NEWSAPI_BASE_URL')}country=us&apiKey={os.getenv('NEWSAPI_KEY')}"
    articles = fetch_news(url)
    return render_template(
        "index.html",
        title="Top Headlines",
        category=ALL_CATEGORIES,
        allNews=articles,
        active_category="General"
    )


@app.route("/<cat>")
def get_category_news(cat):
    url = f"{os.getenv('NEWSAPI_BASE_URL')}country=us&category={cat.lower()}&apiKey={os.getenv('NEWSAPI_KEY')}"
    articles = fetch_news(url)
    return render_template(
        "index.html",
        title=f"{cat} Headlines",
        category=ALL_CATEGORIES,
        allNews=articles,
        active_category=cat
    )

if __name__ == "__main__":
    app.run(debug=True)
