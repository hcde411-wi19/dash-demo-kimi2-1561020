# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.
# initialize Dash app and initialize the static folder
mydateparse = lambda  x: pd.datetime.strptime(x, "%H:%M")
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/babyboom_processed.csv', parse_dates=['Time'], date_parser=mydateparse)

#group by hour
girls = df[df['Sex'] == 1]
#print(girls)
boys = df[df['Sex'] == 2]

dataBoy = [0] * 24
dataGirl = [0] * 24


girls_by_hour = girls.groupby(pd.Grouper(key='Time', freq='1H')).mean().fillna(0)
boys_by_hour = boys.groupby(pd.Grouper(key='Time', freq='1H')).mean().fillna(0)
girls_by_hour.index = girls_by_hour.index.strftime('%H')
girls_by_hour.index.name = 'Hour'
boys_by_hour.index = boys_by_hour.index.strftime('%H')
boys_by_hour.index.name = 'Hour'
#print(boys_by_hour)
#print(girls_by_hour)
for idx, x in boys_by_hour['Sex'].iteritems():
    #print(idx, x)
    idx = int(idx)
    dataBoy[idx] = x

for idx, x in girls_by_hour['Sex'].iteritems():
    idx = int(idx)
    dataGirl[idx] = x

#exit()
#print(dg)

# 1=girl   2=boy

time = list(range(24))

fields = {
    'Girl': dataGirl,
    'Boy': dataBoy
}

# define lines - for each usage data, we create a line series through go.Scatter with mode 'lines+markers'
series = []
for title in fields:
    series.append(
        go.Scatter(
            x=time,
            y=fields[title],
            mode='lines+markers',
            name=title
        )
    )


# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Babyboom in Barisbane, Australia in December 21, 1997'),

    # set the description underneath the heading
    html.Div(children='''
        This visualization is representing the 44 babies born in 24-hour period at a Brisbane, Australia,
hospital. Try to hover over the ilnes to view the number of boys and girls born in each hour. 
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': series,
            'layout': {
                'title': 'Babies Born in 24-Hour Period',
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)