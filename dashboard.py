import dash
import dash_bootstrap_components as dbc
import pandas as pd


df = pd.read_csv("Manhattan_Real_Estate.csv",usecols=['Price','Beds','Baths','Sq Feet','Neighborhood'])

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
app.css.append_css({'external_url':'/static/css.css'})

app.config.suppress_callback_exceptions = True
