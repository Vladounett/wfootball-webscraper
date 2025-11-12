from .scraping import scrape, format_data
from flask import Blueprint, render_template

bp = Blueprint("leagues", __name__)

@bp.route('/WSL')
def wsl_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/womens-super-league/startseite/wettbewerb_ENG1.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Women's super league")

@bp.route('/PL_FRA')
def pl_fra_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/premire-ligue/startseite/wettbewerb_DAN1.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Arkema Première League")

@bp.route('/BUNDES')
def bundes_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/bundesliga/startseite/wettbewerb_BL1.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Frauen-Bundesliga")

@bp.route('/LIGA')
def liga_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/primera-division-femenina/startseite/wettbewerb_ESP1.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Liga F")
    
@bp.route('/SERIEA')
def seriea_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/serie-a-women/startseite/wettbewerb_IT1.htmll"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="Serie A Women")

@bp.route('/NWSL')
def nwsl_data():
        df = format_data(scrape("https://www.soccerdonna.de/en/nwsl/startseite/wettbewerb_NWSL.html"))
        return render_template("league_template.html", tables=[df.to_html(index=False, classes="table table-striped table-bordered")], title="National Women's Soccer League")