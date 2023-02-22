import numpy as np
import pandas
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api_url(station, date):
    station_number = station.zfill(6)
    filename = f"data/TG_STAID{station_number}.txt"

    df = pandas.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    df["TG"] = df["TG0"] / 10

    temperature = df.loc[df["    DATE"] == f"{date}"]["TG"].squeeze()

    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
