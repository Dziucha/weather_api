# import pandas
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api_url(station, date):
    # df = pandas.read_csv("")
    # temperature = df.station(date)
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


app.run(debug=True)
