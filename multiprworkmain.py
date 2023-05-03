import multiprocessing as mp
import socket
from socketserver import ThreadingTCPServer, StreamRequestHandler
from struct import *
import dash
from dash import Dash, html, dcc,ctx,State,Output,Input
from Load import AllStraeamhouse
import Connection
import DASHUSE
import dash_bootstrap_components as dashbootst
PORT=6100
# Define the function that will run in the server process
def Run_server(queue):
    # Set up the server here
    # ...
    hostname = '0.12.182.42'
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((hostname, PORT))
    server_socket.listen(5)

    print('listening on port', PORT);
    while True:
        (client_socket, client_address) = server_socket.accept()

        connect = client_socket
        pacstr = '>' + 'f' * 3
        while 1:
            msg = connect.recv(204)
            if not msg:
                connect.close()
                print(client_address.client_address, 'disconnected')
                break
            print(client_address)

            ar = unpack(pacstr, msg)
            # unpack received data from RTDS, where '>fff' means there are three float type signals are received. 'f' means float type
            print("RX data points: ")
            print(*ar)
            print(len(ar))
            queue.put(ar)
        client_socket.close()
    server_socket.close()
    # Send some data through the queue



# Define the function that will run in the Dash process
def Run_dash(queue):
    # Set up the Dash app here
    app = Dash( external_stylesheets=[dashbootst],)
    app.tile = 'optest'
    app.layout = DASHUSE.create_dash(app)
    app.run_server(host= "127.0.0.1",port=8000 , debug=True,)

    # Get some data from the queue
    # data = queue.get()
    #
    #
    # print(data.houses[1].active)

    # Update the Dash app with the data
    # ...

    # Run the Dash app
    app.run_server(debug=True)


if __name__ == '__main__':
    # Create a queue to share data between processes
    queue = mp.Queue()

    # Create the server process
    server_process = mp.Process(target=Run_server, args=(queue,))

    # Create the Dash process
    dash_process = mp.Process(target=Run_dash, args=(queue,))

    # Start both processes
    server_process.start()
    dash_process.start()

    # Wait for both processes to finish
    server_process.join()
    dash_process.join()

