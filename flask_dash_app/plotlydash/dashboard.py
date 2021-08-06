from dash import Dash
import dash
import dash_core_components as dcc
from dash.dependencies import Input,Output
import dash_html_components as html
import paho.mqtt.client as mqtt
import plotly.express as px
import pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['SmartHome']
db_collection = db['Temperature']

broker_address = '192.168.112.92'
mqtt_client = mqtt.Client("P1")
mqtt_client.connect(broker_address)

data = pd.DataFrame(db_collection.find())

def init_dashboard(server):
    dash_app = dash.Dash(
        server = server,
        routes_pathname_prefix = '/dashapp/',
        external_stylesheets = ''
    )


    dash_app.layout = html.Div([
        dcc.Link('Go to home', href='/', className='link_a'),
        html.Button('Кімната 1(Включити)', id='btn-nclick-1', n_clicks=0, className='first-button', type='checkbox'),
        html.Button('Кімната 1(Виключити)', id='btn-nclick-2', n_clicks=0, type='checkbox'),
        html.Button('Кімната 2(Включити)', id='btn-nclick-3', n_clicks=0, type='checkbox'),
        html.Button('Кімната 2(Виключити)', id='btn-nclick-4', n_clicks=0 ,type='checkbox'),
        dcc.Graph(id='my-graph', figure={}, className = 'graph')
    ], className='general_methods')
    init_dash_app(dash_app)
    return dash_app.server


def init_dash_app(dash_app):

    @dash_app.callback(Output(component_id='my-graph', component_property='figure'),
                  Input(component_id ='btn-nclick-1', component_property = 'n_clicks'),
                  Input(component_id ='btn-nclick-2', component_property = 'n_clicks'),
                  Input(component_id ='btn-nclick-3', component_property =  'n_clicks'),
                  Input(component_id ='btn-nclick-4', component_property =  'n_clicks'))


    def displayClick(btn1, btn2, btn3, btn4):
        broker_address = '192.168.112.92'
        mqtt_client = mqtt.Client("P1")
        mqtt_client.connect(broker_address)
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'btn-nclick-1' in changed_id:
            mqtt_client.publish("lite/topic/1", 0)
        elif 'btn-nclick-2' in changed_id:
            mqtt_client.publish("lite/topic/1", 1)
        elif 'btn-nclick-3' in changed_id:
            mqtt_client.publish("lite/topic/2", "3")
        elif 'btn-nclick-4' in changed_id:
            mqtt_client.publish("lite/topic/2", "4")


        fig1 = px.histogram(data, data["Date and Time"], data["Wind Direction 10 Minutes"])
        return fig1





