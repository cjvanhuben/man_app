import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from dashboard import app,df


PAGE_SIZE = 50

df["Beds"] = df["Beds"].fillna(0)

layout = html.Div([html.H4('Current NYC Apartment Rental Listing'),dash_table.DataTable(
                            css= [{'selector': '.row', 'rule': 'margin: 2px'}],
                            id='table-sorting-filtering',
                            columns=[
                                {'name': i, 'id': i,'deletable':True} for i in df.columns
                            ],
                            data=df.to_dict('records'),
                            style_table={'height':'750px','overflowX': 'scroll'},
                            style_cell={
                                'height': '90',
                                # all three widths are needed
                                'minWidth': '20px', 'width': '20px', 'maxWidth': '20px',
                                'whiteSpace': 'normal'
                            },
                            style_data_conditional=[
                            {
                            'if':{'row_index':'odd'},'backgroundColor':'rgb(248,248,248)'
                            }
                            ],
                            style_cell_conditional=[
                            {'if':{'coloumn_id':'description'},'width':'48%'},
                            {'if':{'coloumn_id':'title'},'width':'18%'}
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
