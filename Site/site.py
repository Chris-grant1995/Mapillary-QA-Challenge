import time
time.sleep(2)
import requests
url = "http://api:80/users"
from datetime import datetime
import pandas;
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.config['suppress_callback_exceptions'] = True
colors = {
    'background': '#EEEEEE',
    'text': '#7FDBFF'
}
request = requests.get(url)
json = request.json()

df = pandas.DataFrame(json["data"])

def getLayout():
    return html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="Person Database Site",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children=[html.Label("Username"),dcc.Input(id='username', type='text')]),
    html.Div(children=[html.Label("Email"),dcc.Input(id='email', type='text')]),
    html.Div(children=[html.Label("Address"),dcc.Input(id='address', type='text')]),
    html.Div(children=[html.Label("Birthday (MM/DD/YYYY)"),dcc.Input(id='birthday', type='text')]),
    html.Button('Create New Person', id='button'),
    html.Div(id='output-container-button',
            children=''),
    html.Div(id='live-update-text'),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )

    ])
    
@app.callback(dash.dependencies.Output('live-update-text', 'children'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def updateTable(n):
    request = requests.get(url)
    json = request.json()
    df = pandas.DataFrame(json["data"])
    return generate_table(df)

def generate_table(dataframe, max_rows=100):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app.layout = getLayout

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('username', 'value'),
    dash.dependencies.State('email', 'value'),
    dash.dependencies.State('address', 'value'),
    dash.dependencies.State('birthday', 'value')])
def update_output(n_clicks, username, email,address,birthday):
    # app.layout = getLayout("new")
    if username == "None" or email == "None" or address == "None" or birthday == "None" :
        return "Every Field must have a value"
    dic = {"username":username, "email":email, "address": address, "birthday" : birthday}
    print(username,email,address,birthday)
    response = requests.post(url,data=dic)
    print(response.json())
    app.layout = getLayout
    return ""
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=False)
