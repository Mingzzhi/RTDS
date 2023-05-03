from dash import html, dcc, Input, Output
from dash_extensions.enrich import  DashProxy
from dash_extensions import WebSocket
import threading as th
import socket
import random as rnd
import time as t
class producer(th.Thread):
    def __init__(self, threadID, port):
        th.Thread.__init__(self)
        self.threadID = threadID
        self.done = False
        self.sleep_time = 0.250
        self.data = []
        self.resetData()
        self.pause = False
        self.fakeRspTime = 0
        self.busy = False
        self.port = port

        # Create a TCP socket and bind it to the specified port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', self.port))





    def stop(self):
        self.done = True

    def run(self):
        while self.done == False:
            # Main loop

            self.server_socket.listen(1)
            client_socket, client_address = self.server_socket.accept()
            while True:
                data = client_socket.recv(1024)
                print("Received from client:", data.decode())
                self.data=data.decode()
                # self.busy = self.__update(timeout=0.150)
                t.sleep(self.sleep_time)
            client_socket.close()
            self.done=True
        # Cleanup

    # def __update(self, timeout=0.250):
    #     """  Here the producer would access some data inbound socket/IO
    #     Faking asynchronous data below.
    #     :param data:
    #     """
    #     # -------------------------
    #     if self.pause:
    #         # Emulate paused, busy
    #         return True
    #     else:
    #         fakeDelay = rnd.randint(1, 4)
    #         if self.fakeRspTime < fakeDelay:
    #             t.sleep(timeout)
    #             self.fakeRspTime = self.fakeRspTime + 1
    #             # Emulate busy
    #             return True
    #         else:
    #             self.fakeRspTime = 0
    #             # Emulate data ready (not busy)
    #             # Emulate updating data from producer
    #             self.data = self.data[0]
    #
    #             return False
        # -------------------------

    def getData(self):
        print("INFO: Data Request. Busy?", self.busy)
        return self.data

    def pauseData(self, state):
        self.pause = state







from dash import Dash
# Create example app.
app = DashProxy(prevent_initial_callbacks=True)
# app=Dash(__name__)
app.layout = html.Div([
    dcc.Input(id="input", autoComplete="off"),
    html.H2(id="message"),
    # WebSocket(url="ws://127.0.0.1:8000/Rrand", id="ws")
])

# @app.callback(Output("ws", "send"), [Input("input", "value")])
# def send(value):
#     return value
#
# @app.callback(Output("message", "children"), [Input("ws", "message")])
# def message(e):
#     print(e)
#     return f"Response from websocket: {e['data']}"

if __name__ == '__main__':
    protes=producer(1,5004)
    protes.start()
    app.run_server()
