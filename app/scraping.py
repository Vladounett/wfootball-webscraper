import pandas as pd

def format_data(data_frame):
    
    data_frame = data_frame.drop([0], axis=1)
    data_frame = data_frame.drop(data_frame.tail(2).index)

    
    data_frame.columns = ["Club", "Squad size", "Average Age", "Market value (€)", "Average Value (€)"]
    
    #getting back the average age with the dot
    if data_frame["Average Age"].astype(float).mean() > 100:
        data_frame["Average Age"] = data_frame["Average Age"].astype(float) / 10
    
    return data_frame

def scrape(url):
    return pd.read_html(url)[1]