from distutils.log import debug
from dash import Dash, html # this only works for Dash v2.0

app = Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),# calling a Dash component
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Sources',
                   href = 'https://worldhappiness.report/',
                   target = '_blank')])
])

if __name__ == '__main__':
    app.run_server(debug = True) # True when developing the App. False when deploying it to production
    # we can think of it as the name of the script file
# when we set up the Dash app with app = dash.Dash() there's a default argument name = '__main__'
# we do this because before we run the server, we want to ensure that this file is run as the main program
