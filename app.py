from flask import Flask, render_template
from rss_sources import get_articles

app = Flask(__name__)

@app.route("/")
def home():
    articles = get_articles()
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
