import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas
from dash.dependencies import Input,Output

from dashboard import app,df


min_p = df.Price.min()
max_p = df.Price.max()
min_b = df.Beds.min()
max_b = df.Beds.max()
min_bath = df.Baths.min()
max_bath = df.Baths.max()

layout = html.Div([

    html.H1('Current NYC Apartment Rental Listings')
    ,dbc.Row([dbc.Col(
        html.Div([

html.Div([html.P('\n'),html.H3('Price')
   ,dcc.RangeSlider(id='price-slider'
                   ,min = min_p
                   ,max= max_p
                   , marks = {0: '$0',

                               10000: '$10,000',
                               20000: '$20,000',
                               30000: '$30,000',
                               40000: '$40,000'

                              }
                   , value = [0,50000]
                   ),
                   html.P('\n'),html.H3('Beds'),
                   dcc.RangeSlider(id='bed-slider'
                                   ,min = min_b
                                   ,max= max_b
                                   , marks = {0: '0',
                                               1: '1',
                                               2: '2',
                                               3: '3',
                                               4: '4',
                                               5:'5'
                                              }
                                   , value = [0,6]
                                   ),
                                   html.P('\n'),html.H3('Baths'),
                                   dcc.RangeSlider(id='bath-slider'
                                                   ,min = min_bath
                                                   ,max= max_bath
                                                   , marks = {0: '0',
                                                               1: '1',
                                                               2: '2',
                                                               3: '3',
                                                               4: '4',
                                                               5:'5'
                                                              }
                                                   , value = [0,6]
                                                   )

                   ]),


        html.H3('Neighborhood'),dcc.Dropdown(id = 'dropdown1',
            options = [{'label': i, 'value':i} for i in df.Neighborhood.unique()],
            multi=True,
            # value = [i for i in df.Neighborhood.unique()]
        ),html.P('\n'),
        html.H3('Borough'),dcc.Dropdown(id = 'dropdown2',
            options = [{'label': i, 'value':i} for i in df.Borough.unique()],
            multi=True,
            # value = [i for i in df.Neighborhood.unique()]
        )

        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15})
    , width=3,id ='side')
,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Data Table', value='tab-1'),
                    dcc.Tab(label='Graphs', value='tab-2'),
                ])
            , html.Div(id='tabs-content')
        ]), width=9)])

    ])
