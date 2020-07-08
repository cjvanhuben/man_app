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

layout = html.Div([

    html.H1('Manhattan Apartments in June')
    ,dbc.Row([dbc.Col(
        html.Div([
         html.Div([html.H3('Price Slider')
            ,dcc.RangeSlider(id='price-slider'
                            ,min = min_p
                            ,max= max_p
                            , marks = {0: '$0',
                                        1000000: '$1,000,000',
                                        2500000: '$2,500,000',
                                        4000000: '$4,000,000',
                                        5500000: '$5,500,000',
                                        7000000: '$7,000,000',
                                        8500000: '$8,500,000'
                                       }
                            , value = [0,10000000]
                            )

                            ])

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
