import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input,Output, State
import plotly.express as px
from pymongo import MongoClient
import pandas as pd
import paho.mqtt.client as mqtt


client = MongoClient('localhost', 27017)
db = client['SmartHome']
db_collection = db['Temperature']

broker_address = '192.168.112.92'
mqtt_client = mqtt.Client("P1")
mqtt_client.connect(broker_address)

data = pd.DataFrame(db_collection.find())


def init_dashboard_temp(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix = '/app_dash_temperature/'
    )



    dash_app.layout = html.Div([
        dcc.Link('Go to home', href='/', className='link_a'),
        dcc.Input(id='input_hemb',
                  type='number',
                  value=20,
                  className='hemb_input'),
        html.Button('Змінити температуру', id='sub_button', n_clicks=0, className='input_button'),
        html.H3(
            'Дана сторінка показує на dashboard температуру в приміщені. Змінити температуру можливо за допомогою віджетів які надані.'),
        dcc.Graph(id='my-graph-2', figure={})
    ])
    init_dash_app(dash_app)
    return dash_app.server


def init_dash_app(dash_app):
    @dash_app.callback(
        Output(component_id='my-graph-2', component_property='figure'),
        Input(component_id='sub_button', component_property='n_clicks'),
        State(component_id='input_hemb', component_property='value')
    )


    def display_fig2(n_clicks, value):
        if n_clicks > 0:
            broker_address = '192.168.112.92'
            mqtt_client = mqtt.Client("P1")
            mqtt_client.connect(broker_address)
            mqtt_client.publish("/test", payload=value, qos=0, retain=False)
        fig = px.line(data, x=data["Date and Time"], y=data["CR10 Temperature"])
        return fig

