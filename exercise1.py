# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# static data
weekday_in_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
counts_in_order = [160613, 154225, 155175, 150819, 146014, 215725, 203483]
# TODO: working on this file to add more codes...
ped_s = [28686, 27520, 27224, 25846, 24900, 37808, 34792]
ped_n = [26884, 26444, 25876, 24368, 23403, 36894, 32792]
bike_s = [52642, 50812, 51866, 50913, 49740, 71586, 68147]
bike_n = [52401, 49449, 50209, 49692, 47971, 69437, 67752]

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a simple Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': weekday_in_order, 'y': counts_in_order, 'type': 'bar', 'name': 'Total'},
                {'x': weekday_in_order, 'y': ped_s, 'type': 'bar', 'name': 'Ped S'},
                {'x': weekday_in_order, 'y': ped_n, 'type': 'bar', 'name': 'Ped N'},
                {'x': weekday_in_order, 'y': bike_s, 'type': 'bar', 'name': 'Bike S'},
                {'x': weekday_in_order, 'y': bike_n, 'type': 'bar', 'name': 'Bike N'},

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Usage of the BGT North of NE 70th per week day'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



