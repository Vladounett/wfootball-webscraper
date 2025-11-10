from .scraping import scrape, format_data
from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

@bp.route('/')
def home():
        return render_template("index.html")

@bp.route('/WSL')
def wsl_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/womens-super-league/startseite/wettbewerb_ENG1.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Women's super league")

@bp.route('/PL_FRA')
def pl_fra_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/premire-ligue/startseite/wettbewerb_DAN1.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Arkema Première League")