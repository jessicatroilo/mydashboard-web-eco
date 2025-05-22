from flask import Flask, render_template
from rss_fetcher import get_articles
from date_manager import DateManager

app = Flask(__name__)
date_manager = DateManager()  # Instanciation

@app.route("/")
def home():
    current_date = date_manager.get_current_date()
    articles = get_articles()
    return render_template("index.html", articles=articles, current_date=current_date)

if __name__ == "__main__":
    app.run(debug=True)