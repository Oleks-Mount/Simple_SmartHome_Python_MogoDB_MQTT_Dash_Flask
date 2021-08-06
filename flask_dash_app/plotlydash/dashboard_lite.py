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
db_collection = db['Humidity']

broker_address = '192.168.112.92'
mqtt_client = mqtt.Client("P1")
mqtt_client.connect(broker_address)

data = pd.DataFrame(db_collection.find())

df = pd.read_csv('C:/Users/oleks/PycharmProjects/Dash_app/data_set/trade.csv')

def init_dashboard_lite(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix = '/app_dash_lite/'
    )

    dash_app.layout = html.Div([
        dcc.Link('Go to home', href='/', className='link_a'),
        dcc.Dropdown(
            id='app-1-dropdown',
            options=[
                {'label': i, 'value': i} for i in sorted(df.Year.unique())],
            value='2015',
            className='lite'),
        dcc.Graph(id='my-graph', figure={})
    ])
    init_dash_app(dash_app)
    return dash_app.server


def init_dash_app(dash_app):

    @dash_app.callback(
        Output(component_id='my-graph', component_property='figure'),
        Input(component_id='app-1-dropdown', component_property='value'))
    def display_value(value):
        dff = df[df.Year == value]
        fig = px.histogram(data_frame=dff, x='Date', y='Value')
        return fig


