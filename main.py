import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

def format(data_frame):
    
    data_frame = data_frame.drop([0], axis=1)
    data_frame = data_frame.drop([12,13])
    
    data_frame.columns = ["Club", "Squad size", "Average Age", "Market value (€)", "Average Value (€)"]
    
    #correction perte virgule
    if data_frame["Average Age"].astype(float).mean() > 100:
        data_frame["Average Age"] = data_frame["Average Age"].astype(float) / 10
    
    return data_frame

def scrape(url):
    return pd.read_html(url)[1]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/WSL')
def wsl_data():
    df = format(scrape("https://www.soccerdonna.de/en/womens-super-league/startseite/wettbewerb_ENG1.html"))
    return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")])

@app.route('/PL_FRA')
def pl_fra_data():
    df = format(scrape("https://www.soccerdonna.de/en/premire-ligue/startseite/wettbewerb_DAN1.html"))
    return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")])

if __name__ == '__main__':
    app.run(debug=True)
    