import requests
import pandas as pd
from bs4 import BeautifulSoup
   
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



if __name__ == '__main__':
    print(format(scrape("https://www.soccerdonna.de/en/womens-super-league/startseite/wettbewerb_ENG1.html")))
    