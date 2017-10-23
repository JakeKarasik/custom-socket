
import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

def init(UDPportTx, UDPportRx):   # initialize your UDP socket here 
    pass 
    
class socket:
    
    def __init__(self):  # fill in your code here 
        return
    
    def bind(self, address):
        return 

    def connect(self, address):  # fill in your code here
    	# Bind
    	# Create the SYN header
    	# Send the SYN packet A
    	# Start timer
    	# recv SYN ACK B
    	# send ACK C
    	# if there is error, send header again
        return 
    
    def listen(self, backlog):
        return

    def accept(self):
    	# recv SYN A
    	# send SYN ACK B
    	# ACK C
        (clientsocket, address) = (1, 1)  # change this to your code 
        return (clientsocket, address)
    
    def close(self):   # fill in your code here 
        return 

    def send(self, buffer):
    	# Create header
    	# Send data
    	# Start timer
    	# If timeout, send same packet again
        bytessent = 0     # fill in your code here 
        return bytessent 

    def recv(self, nbytes):
    	# Packets recv
    	# Send right ACK
        bytesreceived = 0     # fill in your code here
        return bytesreceived 
