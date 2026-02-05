from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "Ace4d41ae67242349c6bf98ca795f17b")

@app.route("/", methods=["GET", "POST"])
def index():
    articles = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            url = "https://newsapi.org/v2/everything"
            params = {
                "q": query,
                "language": "en",
                "pageSize": 5,   # limit results
                "sortBy": "publishedAt",
                "apiKey": NEWS_API_KEY,
            }
            response = requests.get(url, params=params)
            data = response.json()

            # If API works, extract articles
            if data.get("status") == "ok":
                articles = data.get("articles", [])

    return render_template("news.html", articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)