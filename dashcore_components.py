
from dash import Dash, html, dcc # this only works for Dash v2.0
import pandas as pd
import plotly.express as px

data = pd.read_csv('data/world_happiness.csv')

linefig = px.line(data[data['country'] == 'United States'], x = 'year', y = 'happiness_score', title = 'Happiness Score in the USA')

app = Dash()

# app layout
app.layout = html.Div([
    html.H1('World Happiness Dashboard'),# calling a Dash component
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Sources',
                   href = 'https://worldhappiness.report/',
                   target = '_blank')]),
    # let´s add the dash core components now (dcc)
    dcc.RadioItems(options = data['region'].unique(), value = 'Central and Eastern Europe'),
    dcc.Checklist(options = data['region'].unique(), value = ['Central and Eastern Europe']),
    dcc.Dropdown(options = data['country'].unique(), value = 'Finland'),
    dcc.Graph(figure = linefig)
    # we can pass the options as an array
    # we can pass the options as a dictionary. the keys don't appear. the values are the labels that users can see
    # we can get it from a dataframe
])


if __name__ == '__main__':
    app.run_server(debug = True)