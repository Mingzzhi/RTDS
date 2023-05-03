import socket
import struct
import time
import random
from Network import calculteDss
from Load import Readfilesepare
# Define the server's IP address and port number
SERVER_IP = '127.0.0.1'
    # socket.gethostname()
SERVER_PORT = 8000

# Define the number of floats to send and receive per second
NUM_FLOATS_PER_SEC = 3
data_array = [0.1109592, -0.0774576, 0.0242556, -0.1598016, 0.035745, -0.0314556, 0.3658752, -0.156021, 0.1684332, 0.0421083, 0.0910391, 0.0563349, 0.009512, 0.0, 0.0, -0.05955, 0.152391, -0.237474, 0.2295658, 0.0906868, 0.1950606, 0.1309896, 0.049266, -0.100436, 0.0347772, -0.123864, 0.287859, 0.0, 0.040426, -0.171216, 0.4098545, -0.2968075, 0.368784, 0.0, 0.01189, 0.0, 0.0064287, -0.0069049, 0.3648969, 0.1766395, 0.0397992, -0.3603249, 0.0, -0.059525, 0.007131, 0.0, 0.0550536, -0.1891281, 238.07, 237.99, 237.64]

# Define the struct format for packing and unpacking the floats
FLOAT_STRUCT_FORMAT = '>' + 'f' * NUM_FLOATS_PER_SEC
def genrand(up,down):
    return random.uniform(down,up)
# B5 is active
# houseb1=[genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5)]
# houseb2=[genrand(10,-5),genrand(10,-5)]
# houseb3=[genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5)]
# houseb4=[genrand(10,-5),genrand(10,-5)]
# houseb5=[genrand(calculteDss(data_array))]
# houseb6=[genrand(10,-5),genrand(10,-5)]
# houseb7=[genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5)]
# houseb8=[genrand(10,-5),genrand(10,-5)]
# houseb9=[genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5)]
# houseb10=[genrand(10,-5),genrand(10,-5)]
# houseb11=[genrand(10,-5),genrand(10,-5)]
# houseb12=[genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5),genrand(10,-5)]
# houseb13=[genrand(10,-5),genrand(10,-5)]
# houseb14=[genrand(10,-5),genrand(10,-5)]






# Create a TCP socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f'Connected to server at {SERVER_IP}:{SERVER_PORT}')
except ( TimeoutError):
    print(f'Failed to connect to server at {SERVER_IP}:{SERVER_PORT}')
    exit()
except(OSError):
    print("os error")
    exit()
except(ConnectionRefusedError):
    print("connext refuse")

# Set the socket to non-blocking mode
client_socket.setblocking(False)

# Define the current time and the last time a packet was sent
current_time = time.monotonic()
last_send_time = current_time

# Define the buffer for receiving data from the server
recv_buffer = bytearray()

# Define the total number of bytes we need to receive
total_bytes_to_receive = struct.calcsize(FLOAT_STRUCT_FORMAT)



# checking file is loading

Profiledata=Readfilesepare();
sol=calculteDss(data_array)
print( Profiledata==None)



# Loop until the program is terminated or an exception is encountered
while True:
    # Get the current time
    current_time = time.monotonic()

    # Calculate the time elapsed since the last packet was sent
    time_elapsed = current_time - last_send_time
    # B5 is active
    houseb1 = [genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5)]
    houseb2 = [genrand(10, -5), genrand(10, -5)]
    houseb3 = [genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5)]
    houseb4 = [genrand(10, -5), genrand(10, -5)]

    houseb5 = [genrand(sol[0],sol[1]),genrand(10, -5)]
    houseb6 = [genrand(10, -5), genrand(10, -5)]
    houseb7 = [genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5)]
    houseb8 = [genrand(10, -5), genrand(10, -5)]
    houseb9 = [genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5)]
    houseb10 = [genrand(10, -5), genrand(10, -5)]
    houseb11 = [genrand(10, -5), genrand(10, -5)]
    houseb12 = [genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5), genrand(10, -5)]
    houseb13 = [genrand(10, -5), genrand(10, -5)]
    houseb14 = [genrand(10, -5), genrand(10, -5)]
    housebvol=[genrand(240, 220), genrand(240, 220),genrand(240, 220)]
    Allhouses=[]
    Allhouses=Allhouses+houseb1+houseb2+houseb3+houseb4+houseb5+houseb6+houseb7+houseb8+houseb9+houseb10+houseb11+houseb12+houseb13+houseb14+housebvol

    floats_to_send ="hihell"
        # [houseb1,houseb2,houseb3,houseb4,houseb5,houseb6,houseb7,houseb8,houseb9,houseb10,houseb11,houseb12,houseb13,houseb14,housebvol]

    # If enough time has elapsed, send a packet of floats to the server
    # if time_elapsed >= 5 :
    #     # Create a list of floats to send to the server
    #
    #
    #     # Pack the floats into a binary format
    #     packed_floats = struct.pack(FLOAT_STRUCT_FORMAT, *floats_to_send)
    #
    #     # Send the packed floats to the server
    #     try:
    #         client_socket.sendall(packed_floats)
    #     except (BrokenPipeError, ConnectionResetError, OSError):
    #         print('Failed to send data to the server')
    #         break
    #
    #     # Update the last send time
    #     last_send_time=current_time

    # Receive any data that the server has sent
    try:
        recv_data = client_socket.recv(1024)
    except (socket.timeout, BlockingIOError):
        # No data has been received yet, so continue the loop
        print(BlockingIOError)
    except (BrokenPipeError, ConnectionResetError, OSError):
        print('Failed to receive data from the server')
        break

    # If the server has closed the connection, exit the loop
    if len(recv_data) == 0:
        print('Server has closed the connection')
        break

    # Append the received data to the buffer
    recv_buffer.extend(recv_data)

    # If we have received all the data we need, unpack it and print it
    while len(recv_buffer) >= total_bytes_to_receive:
        # Unpack the floats from the buffer
        unpacked_floats = struct.unpack(FLOAT_STRUCT_FORMAT, recv_buffer[:total_bytes_to_receive])

        # Remove the unpacked floats from the buffer
        recv_buffer = recv_buffer[total_bytes_to_receive:]

        # Print the unpacked floats
        print('Received floats:', unpacked_floats)

# Close the socket
client_socket.close()
