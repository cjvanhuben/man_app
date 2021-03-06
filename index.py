import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import dash_table
import plotly.graph_objs as go

from dashboard import app
from dashboard import df
import sidepanel
import Tab1
import Tab2


#set the app.layout
app.layout = sidepanel.layout

server = app.server


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        # return None
        return Tab1.layout
    elif tab == 'tab-2':
        return Tab2.layout



operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3

@app.callback(
    Output('table-sorting-filtering', 'data'),
    [Input('table-sorting-filtering', "page_current"),
     Input('table-sorting-filtering', "page_size"),
     Input('table-sorting-filtering', 'sort_by'),

     Input('table-sorting-filtering', 'filter_query'),
     Input('dropdown1','value'),
     Input('dropdown2','value'),
     Input('price-slider', 'value'),
     Input('bed-slider','value'),
     Input('bath-slider','value')

      ])

def update_table(page_current, page_size, sort_by, filter,drop1,drop2,prices,bed,bath):
    filtering_expressions = filter.split(' && ')
    dff = df

    low = prices[0]
    high = prices[1]
    blow = bed[0]
    bhigh=bed[1]
    bathlow=bath[0]
    bathhigh=bath[1]


    dff = dff.loc[(dff['Price'] >= low) & (dff['Price'] <= high)]
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


    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value,na=False)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')


if __name__ == "__main__":
    app.run_server(debug = False)
