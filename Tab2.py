import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
import dash_table
from dashboard import app,df


layout = html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )

@app.callback(Output('table-paging-with-graph-container', "children"),
[Input('price-slider', 'value'),
Input('bed-slider','value'),
Input('bath-slider','value'),
Input('dropdown1','value'),
Input('dropdown2','value')
])

def update_graph(prices,bed,bath,drop1,drop2):
    dff = df
    dff["Beds"] = dff["Beds"].fillna(0)
    low = prices[0]
    high = prices[1]
    dff = dff.loc[(dff['Price'] >= low) & (dff['Price'] <= high)]

    blow = bed[0]
    bhigh=bed[1]
    bathlow=bath[0]
    bathhigh=bath[1]


    dff = dff.loc[(dff['Beds'] >= blow) & (dff['Beds'] <= bhigh)]
    dff = dff.loc[(dff['Baths'] >= bathlow) & (dff['Baths'] <= bathhigh)]



    if drop1 == None or drop1 == []:
        pass
    else:
        dff = dff.loc[dff['Neighborhood'].isin(drop1)]
    if drop2 == None or drop2 == []:
        pass
    else:
        dff = dff.loc[dff['Borough'].isin(drop2)]

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
                        , text= dff['Address']
                        , name='Rent v Baths'
                    )
    trace2 = go.Scattergl(x = dff['Beds']
                        , y = dff['Price']
                        , mode='markers'
                        , opacity=0.7
                        , marker={
                                'size': 8
                                , 'line': {'width': 0.5, 'color': 'white'}
                                }
                        , name='Rent v Baths'
                    )
    trace3 = go.Violin(y=dff['Price'], x = dff['Borough'],
     box_visible = True,line_color = 'blue',meanline_visible=True,fillcolor='lightseagreen',opacity=.5,x0='Rent'
    )

    
    return html.Div([
        dcc.Graph(
            id='bath-price'
            , figure={
                'data': [trace1],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'Baths'},
                    yaxis={'title': 'Rent','tickformat':'$0,000'},
                    # margin={'l': 60, 'b': 40, 't': 40, 'r': 10},
                    title='Rent by Bathroom',
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    , html.P('\n'),
    dcc.Graph(
        id='bed-price'
        , figure={
            'data': [trace2],
            'layout': dict(
                xaxis={'title': 'Beds'},
                yaxis={'title': 'Rent','tickformat':'$0,000'},
                title='Rent by Bedroom',
                # margin={'l': 60, 'b': 40, 't': 40, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }

    ),html.P('\n'),
    dcc.Graph(
        id='violin'
        , figure={
            'data': [trace3],
            'layout': dict(
                xaxis={'title': 'Borough'},
                yaxis={'title': 'Rent','range':[0,10000],'tickformat':'$0,000'},

                title='Rent Distribution by Borough',
                # margin={'l': 60, 'b': 40, 't': 40, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }

    )


    ],style={'margin':'15px'})
