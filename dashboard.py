import dash
import dash_bootstrap_components as dbc
import pandas as pd


df = pd.read_csv("NYC_Apts_Rental_Listing.csv",usecols=['Price','Beds','Baths','Neighborhood','Address','Borough','Area'])

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
app.css.append_css({'external_url':'/static/css.css'})

app.config.suppress_callback_exceptions = True
