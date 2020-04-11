from flask import Flask, render_template
from data import predicted, actual, headlines, dates

app = Flask(__name__)

skip = 5  # so the chart is not crowded


@app.route("/")
def home():
    return render_template("index.html",
                           headlines=headlines[::skip],
                           predicted=predicted[::skip],
                           actual=actual[::skip],
                           dates=dates[::skip])


if __name__ == '__main__':
    app.run(debug=True)
