import dash_daq as daq
import dash
from dash import html
from dash import dcc,ctx
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import random
import time
from PIL import Image
from collections import deque

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div(dcc.Graph(id='live-graph'),style={'position': 'fixed', 'top': '100px', 'left': '500px',  'width': '500px', 'height': '300px'}),
    html.Div(
        [
                dcc.Interval(
                id='interval-component',
                interval=10000,
                n_intervals=0
            ),
            html.Header(
                id='leddis',
            )
        ],
        style={'position': 'fixed', 'top': '40px', 'left': '500px', 'width': '200px', 'height': '40px'}
    ),
    html.Div([
        html.Img(src=Image.open('HOUSE1.pic.jpg'), alt='image',id='House1',n_clicks=0,),
    ], style={'position': 'fixed','top': '100px', 'left': '200px'}),
    html.Div([
        html.Img(src=Image.open('HOUSE1.pic.jpg'), alt='image',id='House2',n_clicks=0,),
    ], style={'position': 'fixed','top': '300px', 'left': '200px'}),
    html.Div([
        html.Img(src=Image.open('HOUSE1.pic.jpg'), alt='image',id='House3',n_clicks=0,),
    ], style={'position': 'fixed','top': '500px', 'left': '200px'}),
], style={'max-width': '2000px', 'height': '1000px'})


data_dict = {
        'House1': {'Active Power': deque([0] * 10, maxlen=10), 'Reactive Power': deque([0] * 10, maxlen=10)},
        'House2': {'Active Power': deque([0] * 10, maxlen=10), 'Reactive Power': deque([0] * 10, maxlen=10)},
        'House3': {'Active Power': deque([0] * 10, maxlen=10), 'Reactive Power': deque([0] * 10, maxlen=10)}
    }
timestamps = deque([time.time()] * 10, maxlen=10)

@app.callback(Output('leddis', 'children'),
              Input('House1', 'n_clicks'),
              Input('House2', 'n_clicks'),
              Input('House3', 'n_clicks'))
def set_dropdown_value(button1_clicks, button2_clicks, button3_clicks):
    triggered_id = ctx.triggered_id
    if not triggered_id:
        return triggered_id

    if triggered_id == 'House1':
        return triggered_id
    elif triggered_id == 'House2':
        return triggered_id
    elif triggered_id == 'House3':
        return triggered_id
    else:
        return 'House1'

@app.callback(Output('live-graph', 'figure'),
              Input('interval-component', 'n_intervals'),
              State('leddis','children'))
def update_graph(n, value):
    y1 = random.randint(0, 100)
    y2 = random.randint(0, 100)
    data_dict['House1']['Active Power'].append(y1)
    data_dict['House1']['Reactive Power'].append(y2)
    y3 = random.randint(0, 100)
    y4 = random.randint(0, 100)
    data_dict['House2']['Active Power'].append(y3)
    data_dict['House2']['Reactive Power'].append(y4)
    y5 = random.randint(0, 100)
    y6 = random.randint(0, 100)
    data_dict['House3']['Active Power'].append(y5)
    data_dict['House3']['Reactive Power'].append(y6)
    timestamps.append(time.time())
    triggered_id = ctx.triggered_id
    print(value)
    if value == 'House1':
        Record=triggered_id
        trace1 = go.Scatter(
            x=list(timestamps),
            y=list(data_dict[triggered_id]['Active Power']),
            mode='lines+markers',
            name='Active Power'
        )
        trace2 = go.Scatter(
            x=list(timestamps),
            y=list(data_dict[triggered_id]['Reactive Power']),
            mode='lines+markers',
            name='Reactive Power'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='House 1',
            xaxis=dict(title='Time',range=[min(timestamps), max(timestamps)]),
            yaxis=dict(title='Value', range=[0, 100])
        )
    elif value == 'House2':
        Record=triggered_id
        trace1 = go.Scatter(
            x=list(timestamps),
            y=list(data_dict[triggered_id]['Active Power']),
            mode='lines+markers',
            name='Active Power'
        )
        trace2 = go.Scatter(
            x=list(timestamps),
            y=list(data_dict[triggered_id]['Reactive Power']),
            mode='lines+markers',
            name='Reactive Power'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='House 2',
            xaxis=dict(title='Time',range=[min(timestamps), max(timestamps)]),
            yaxis=dict(title='Value', range=[0, 100])
        )
    elif value == 'House3':
        Record=triggered_id
        trace1 = go.Scatter(
            x=list(timestamps),
            y=list(data_dict[triggered_id]['Active Power']),
            mode='lines+markers',
            name='Active Power'
        )
        trace2 = go.Scatter(
            x=list(timestamps),
            y=list(data_dict[triggered_id]['Reactive Power']),
            mode='lines+markers',
            name='Reactive Power'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='House 3',
            xaxis=dict(title='Time',range=[min(timestamps), max(timestamps)]),
            yaxis=dict(title='Value', range=[0, 100])
        )
    # elif triggered_id=='interval-component' :
    #     trace1 = go.Scatter(
    #         x=list(timestamps),
    #         y=list(data_dict[Record]['Active Power']),
    #         mode='lines+markers',
    #         name='Active Power'
    #     )
    #     trace2 = go.Scatter(
    #         x=list(timestamps),
    #         y=list(data_dict[Record]['Reactive Power']),
    #         mode='lines+markers',
    #         name='Reactive Power'
    #     )
    #     data = [trace1, trace2]
    #     layout = go.Layout(
    #         title='House 1',
    #         xaxis=dict(title='Time', range=[min(timestamps), max(timestamps)]),
    #         yaxis=dict(title='Value', range=[0, 100])
    #     )


    fig = go.Figure(data=data, layout=layout)
    return fig



if __name__ == '__main__':
    app.run_server(debug=True, port=8030)

