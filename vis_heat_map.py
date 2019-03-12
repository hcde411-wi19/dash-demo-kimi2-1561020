# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_json('static/bgt_bike_and_peds.json')

# Data clean up
for col in df.columns:
    if col == "Date":
        continue
    df[col] = df[col].replace(r'', np.nan, regex=True)
    df[col] = df[col].fillna(0)
    df[col] = pd.to_numeric(df[col])

# Group by month
dg = df.groupby(pd.Grouper(key='Date', freq='1M')).sum()
dg.index = dg.index.strftime('%Y-%m')
dg.index.name = 'Month'

exclude = ['Date', 'BGT North of NE 70th Total']
fields = [title for title in list(dg) if title not in exclude]
# define z, which contains the values that we use "heat" to represent
z = dg[dg["Ped South"], dg["Ped North"], dg["Bike South"], dg["Bike North"]
z = []
for idx, field in enumerate(fields):
    z.append(dg[field])

# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Heatmap'),

    # set the description underneath the heading
    html.Div(children='''
        A demo to show a heatmap.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how a heatmap is defined -- x is the same as the one we had in the line chart
                # y is break down usage, and z is the corresponding counts over time
                go.Heatmap(z=z,
                           x=dg.index,
                           y=fields)
            ],
            'layout': {
                'title': 'Monthly usage break down of the BGT North of NE 70th over time',
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)