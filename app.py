from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=976562080a5c40258657cb3a0a714ca9"
    try:
        r = requests.get(url).json()
        articles = r.get('articles', [])   # ✅ Safe way to get articles
    except Exception as e:
        articles = []
        print("Error fetching news:", e)
    
    return render_template('index.html', allNews=articles)

if __name__ == '__main__':
    app.run(debug=True)
