import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from dashboard import app,df


PAGE_SIZE = 100

df["Beds"] = df["Beds"].fillna(0)

layout = html.Div([html.H4('Current NYC Apartment Rental Listing'),dash_table.DataTable(
                            css= [{'selector': '.row', 'rule': 'margin: 2px'}],
                            id='table-sorting-filtering',
                            columns=[
                                {'name': i, 'id': i,'deletable':True} for i in df.columns
                            ],
                            style_table={'height':'750px','overflowX': 'scroll'},
                            style_cell={
                                'whiteSpace':'normal',
                                'height': 'auto',
                                # all three widths are needed
                                # 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',

                            },

                            style_data_conditional=[
                            {
                            'if':{'row_index':'odd'},'backgroundColor':'rgb(248,248,248)'
                            }
                            ],

                            page_current= 0,
                            page_size= PAGE_SIZE,
                            page_action='custom',
                            filter_action='custom',
                            filter_query='',

                            sort_action='custom',
                            sort_mode='multi',
                            sort_by=[]
                            )],

                        style={'margin':'15px'}
                        )
