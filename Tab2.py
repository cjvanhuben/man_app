import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from dashboard import app,df


layout = html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )

@app.callback(Output('table-paging-with-graph-container', "children"),
[Input('price-slider', 'value')
])

def update_graph(prices):
    dff = df
    low = prices[0]
    high = prices[1]
    dff = dff.loc[(dff['Price'] >= low) & (dff['Price'] <= high)]

    # if ratingcheck == ['Y']:
    #    dff = dff.loc[dff['rating'] >= 95]
    # else:
    #     dff
    trace1 = go.Scattergl(x = dff['Baths']
                        , y = dff['Price']
                        , mode='markers'
                        , opacity=0.7
                        , marker={
                                'size': 8
                                , 'line': {'width': 0.5, 'color': 'white'}
                                }
                        , name='Price v Baths'
                    )
    return html.Div([html.H4('Price by Bathroom'),
        dcc.Graph(
            id='bed-price'
            , figure={
                'data': [trace1],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'Baths'},
                    yaxis={'title': 'Price'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ],style={'margin':'15px'})
