import random
import time

import dash
from dash import Dash, html, dcc,ctx,State,Output,Input
import plotly.express as px

import pandas as pd
import numpy as np
import dash_bootstrap_components as dashbootst

import Load
from PIL import Image
from Load import AllStraeamhouse
import plotly.graph_objects as go


from struct import *
import multi_infor




PORT = 6100;

## Initialization

optime = 0
Currenttime = 0
Streamhouse = Load.AllStraeamhouse()
Alloefile = Load.Readfilesepare()

OEactiveini = Load.Dssdata(Alloefile[optime])
OEforpssive = [10, -5]
OEtimelist = []
OEtimelist.append(0)
OEtimelist.append(time.monotonic() + 300)
currentoutput = Load.LoadStream(Currenttime)
Streamhouse.extractor(currentoutput, time.monotonic())

OEactiveCal_list = OEactiveini
OEactiveDis_listUp = [OEactiveini[0],OEactiveini[0]]
OEactiveDis_listDown = [OEactiveini[1],OEactiveini[1]]

app = Dash(__name__ ,external_stylesheets=[dashbootst])





def create_dash(app: Dash) -> html.Div:

    return html.Div(className='firstdive',
                    children=[

                              html.H3(style={'background-image': 'url(/assets/finallay.pic.jpg)','background-size': '100% 100%','background-repeat':'no-repeat','background-size':'cover' ,'position': 'absolute','top': '1px', 'left': '2px','height':'800px','width':'1400px',}),
                              # html.Div([
                              #     html.Img(src=Image.open('finallay.pic.jpg') , alt='image', id='House1', n_clicks=0 ,style={'position': 'absolute','top': '0px', 'left': '10px','height':'800px','width':'1400px',}),
                              # ],),

                              dcc.Link(children="go to next ",href='/Dashpage2' ,style={'position': 'absolute','top': '400px', 'left': '1600px','height':'80px','width':'14px'}),
                              # multi_infor.B1info(app,Streamhouse),
                              # rendbotton(app),
                              # Secondgrahp(app),
                              # firstgrahp(app),


                              ],style={'width': '1300px', 'height': '800px',})




def rendbotton(app:Dash)  -> html.Div:




    return html.Div(className='dropdown',
                                       children=[
                                           dcc.Dropdown([Streamhouse.houses[i].name for i in range(len(Streamhouse.houses))], id='powerdrop',)],style={'position': 'absolute','top': '10px', 'left': '1700px','height':'50px','width':'800px'})

# def Secondgrahp(app: Dash)->html.Div:
#
#
#
#
#     return html.Div(className=" grapharea",children=[dcc.Graph(id="Voltagegraph",config={'autosizable':True})]
#                                                       , style={'position': 'absolute', 'top': '390px', 'left': '1600px', 'height': '290px', 'width': '1000px',})
#
# #
#
# def firstgrahp(App: Dash) :
#
#
#
#     return html.Div(className='OE_graph',children=[dcc.Graph(id="OEGRAPH"
#         ,config={'autosizable':True}),dcc.Interval(id="TimeforOE",interval=278300,n_intervals=0),dcc.Interval(id="Timeforreal",interval=2513,n_intervals=0)], style={'position': 'absolute','top': '60px', 'left': '1600px','height':'290px','width':'1000px','backgroundColor':'black'})
#

# @app.callback(
#
#     Output(component_id="OEGRAPH", component_property="figure" ),
#     Input(component_id="TimeforOE", component_property="n_intervals"),
#     Input(component_id="Timeforreal", component_property="n_intervals"),
#     Input(component_id="powerdrop", component_property="value"),
# )
# def Timeupdate(oen,realn,value):
#
#     triggered_id = ctx.triggered_id
#
#
#     layout = go.Layout(
#         title="Operation envelop and Voltage",
#         xaxis=dict(title='Time'),
#         yaxis=dict(title='KW Kilowatt in real time', range=[-15,15]),
#         plot_bgcolor='rgba(240,240,240, 0.7)',
#         paper_bgcolor='rgba(0, 0, 50, 0.7)',
#         height=400,
#         width=1000
#
#     )
#     dataini=go.Scatter(x=[],y=[])
#     global Currenttime,optime,Streamhouse,OEtimelist,OEactiveDis_listUp,OEactiveDis_listDown,OEactiveCal_list
#     currendrop=value
#
#     if triggered_id == "Timeforreal":
#
#         Currenttime = Currenttime+1
#         currentoutput=Load.LoadStream(Currenttime)
#
#         Streamhouse.extractor(currentoutput,time.monotonic())
#
#
#     if triggered_id=="TimeforOE":
#         optime=optime+1
#         OEtimelist.append(time.monotonic())
#         OEtimelist.append(time.monotonic() + 300)
#         print("h")
#         OEactiveC=Load.Dssdata(Alloefile[optime])
#         OEactiveCal_list = OEactiveCal_list + OEactiveC
#         print("y")
#         for i in range(len(OEtimelist)):
#             if i % 2 ==0 or i==0:
#                 OEactiveDis_listUp.append(OEactiveCal_list[i])
#                 OEactiveDis_listUp.append(OEactiveCal_list[i])
#
#
#         else:
#                 OEactiveDis_listDown.append(OEactiveCal_list[i])
#                 OEactiveDis_listDown.append(OEactiveCal_list[i])
#
#
#     if value is not None and value != 'B5':
#         house=Streamhouse.findhouse(value)
#
#         lineOE_UP = go.Scatter(x=OEtimelist, y=[OEforpssive[0]]*len(OEtimelist),mode='lines+markers',name="OE_export")
#         lineOE_Down = go.Scatter(x=OEtimelist, y=[OEforpssive[1]]*len(OEtimelist),mode='lines+markers',name="OE_import")
#
#         Cstream=go.Scatter(x=Streamhouse.time,y=house.active[0:len(Streamhouse.time)],mode='lines+markers',name="active_power")
#
#         return {'data': [lineOE_UP,lineOE_Down,Cstream], 'layout': layout}
#     elif value is not None and value == 'B5':
#         house=Streamhouse.findhouse(value)
#         lineOE_UP=go.Scatter(x=OEtimelist,y=OEactiveDis_listUp,mode='lines+markers',name="OE_import")
#         lineOE_Down=go.Scatter(x=OEtimelist,y=OEactiveDis_listDown,mode='lines+markers',name="OE_export")
#         Cstream = go.Scatter(x=Streamhouse.time,y=house.active[0:len(Streamhouse.time)],mode='lines+markers',name="active_power")
#
#         return {'data': [lineOE_UP,lineOE_Down,Cstream], 'layout': layout}
#
#     return {'data': [dataini], 'layout': layout}
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
#
#
#
#
#
#
#
#
#
# @app.callback(
#     Output(component_id="Voltagegraph",component_property="figure"),
#     Input(component_id="powerdrop",component_property='value'),
#     Input(component_id="Timeforreal", component_property="n_intervals"),
# )
# def Timeupdate(value,n):
#
#
#     triggered_id = ctx.triggered_id
#     print(triggered_id)
#     print(value,n)
#     record=value
#     layout = go.Layout(
#
#         xaxis=dict(title='Time'),
#         yaxis=dict(title='Voltage graph', range=[220,240]),
#         plot_bgcolor='rgba(240,240,240, 0.7)',
#         paper_bgcolor='rgba(0, 0, 50, 0.7)',
#         height=400,
#         width=1000
#     )
#     dataini=go.Scatter(x=[],y=[])
#
#     if value is not None and triggered_id=="Timeforreal" :
#         print(record)
#         house = Streamhouse.findhouse(value)
#         fig=go.Scatter(x=Streamhouse.time,y=house.voltage[0:len(Streamhouse.time)],mode='lines+markers',name='Voltage')
#
#         return {'data': [fig], 'layout': layout }
#
#
#
#     return {'data':[dataini],'layout':layout}
#
#
#










if __name__ == '__main__':
    app.tile = 'optest'
    app.layout = create_dash(app)

    app.run(debug=True)

