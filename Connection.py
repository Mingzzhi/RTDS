# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:31:31 2021

@author: Zoe
"""
import os
import socket
import socketserver
import time
from socketserver import ThreadingTCPServer, StreamRequestHandler
from struct import *
import datetime


import Load

import random

from dash import Dash, html, dcc,ctx,State
import plotly.express as px
import dash_renderer as Dashrender
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
import dash_bootstrap_components as dashbootst



import queue
import plotly.graph_objects as go

PORT = 6110;  # TCP server port ID


# app = Dash(external_stylesheets=[dashbootst])
# app.tile = 'optest'

class RequestHandler(StreamRequestHandler):

    def handle(self):

        ar2 = []
        for w in range(2):
            ar2.append(0.0)
        print (ar2);
        print('connection from', self.client_address)
        conn = self.request
        pacstr = '>' + 'f' * 51
        while 1:
            msg = conn.recv(204)
            if not msg:
                conn.close()
                print (self.client_address, 'disconnected')
                break
            print (self.client_address)

            ar = unpack(pacstr, msg)
            #unpack received data from RTDS, where '>fff' means there are three float type signals are received. 'f' means float type
            print("RX data points: ")
            print (*ar)
            print(len(ar))
            queue.put(ar)
            # StreamRecord.extractor(ar,time.monotonic())


    
            msg2 = pack('>ff', ar2[0], ar2[1]) #pack control signal and send it to RTDS
            
            conn.send(msg2)
            print("%8.3f" % ar2[0], "%8.3f" % ar2[1]); print("---")


def returnstream():
    return StreamRecord

# def main() -> None:
#
#     app.layout = DASHUSE.create_dash(app,StreamRecord)
#     app.run(debug=True,port=8200)
#     hostname = socket.gethostname()
#     with ThreadingTCPServer((hostname, PORT), RequestHandler) as server :
#         print('listening on port', PORT);
#         server.serve_forever()



if __name__ == '__main__':

    hostname = socket.gethostname()
    with ThreadingTCPServer((hostname, PORT), RequestHandler) as server:
        print('listening on port', PORT);
        server.serve_forever()









#
# @app.callback(
#     Output(component_id="firstgraph", component_property="figure"),
#     Input(component_id="intervalset", component_property="n_intervals"),
#     prevent_initial_call=False)
# def Timeupdate(n):
#     timeserise = np.array(StreamRecord.houses[14].time)
#     timeserise = np.zeros(100)
#     VoltageNp = np.zeros((3, len(StreamRecord.houses[14].time)))
#     for i in range(len(StreamRecord.houses)):
#         if StreamRecord.houses[i].name == "B15":
#             VoltageNp = StreamRecord.houses[i].voltage[0:3, len(StreamRecord.houses[14].time)]
#
#     triggered_id = ctx.triggered_id
#     print(triggered_id)
#     layout = go.Layout(
#
#         xaxis=dict(title='Time'),
#         yaxis=dict(title='Value', range=[210, 250]),
#
#     )
#     plot = go.Scatter(x=timeserise, y=VoltageNp[0, :])
#     fig = go.Figure(plot)
#     # for j in range(0,3):
#     #     fig.add_trace(go.Scatter(x=timeserise,y=VoltageNp[j,:], mode='lines+markers', name='volatage'))
#
#     return html.Div(className=" grapharea", id="firstgraph",children=[dcc.Graph(figure=fig , config={'autosizable': True})],
#                     style={'position': 'absolute', 'top': '600px', 'left': '1400px', 'height': '500px',
#                            'width': '1000px'})




