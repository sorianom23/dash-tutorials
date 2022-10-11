from dash import Dash, html, dcc, Input, Output # this only works for Dash v2.0
import pandas as pd
import plotly.express as px

app = Dash()

app.layout = html.Div([
    dcc.Input(id = 'input-text', value = '', type = 'text'),
    # id = each component needs to have a unique id name
    # value = what displays first when we launch the dashboard
    # type = controls what the user can put in the input box
    html.Div(children = '', id = 'output-text')
])

@app.callback(
    Output(component_id =  'output-text', component_property = 'children'),
    Input(component_id = 'input-text' , component_property = 'value')
)
def update_text(input_text):
    return input_text

if __name__ == '__main__':
    app.run_server(debug = True)