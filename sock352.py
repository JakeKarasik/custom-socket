
import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

def init(UDPportTx, UDPportRx):   # initialize your UDP socket here
    # UDP Port
    global RECV_PORT, SEND_PORT
    RECV_PORT = UDPportTx
    SEND_PORT = UDPportRx

    # Header Default
    global PKT_HEADER_DATA, HEADER_LEN, VERSION, OPT_PTR, PROTOCOL, SRC_PORT, DEST_PORT, WINDOW, CHECKSUM
    PKT_HEADER_DATA = struct.Struct('!BBBBHHLLQQLL')
    HEADER_LEN = sys.getsizeof(PKT_HEADER_DATA)
    VERSION = 0x1
    OPT_PTR = 0
    PROTOCOL = 0
    SRC_PORT = 0
    DEST_PORT = 0
    WINDOW = 0 # Unused for part 1
    CHECKSUM = 0 # Unused for part 1

    # Flags
    global SYN, FIN, ACK, RES, OPT
    SYN = 0b00000001
    FIN = 0b00000010
    ACK = 0b00000100
    RES = 0b00001000
    OPT = 0b00010000

class socket:
    
    def __init__(self):  # fill in your code here 
        self.sock = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
    
    def bind(self, address):
        return 

    def connect(self, address):  # fill in your code here
    	# Bind < NO
    	# Create the SYN header
    	# Send the SYN packet A
    	# Start timer
    	# recv SYN ACK B
    	# send ACK C
    	# If there is error, send header again


        self.sock.connect(address)
        seq_num = 0
        ack_num = seq_num + 1
        payload_len = 0

        header = PKT_HEADER_DATA.pack(  VERSION,
                                        SYN,
                                        OPT_PTR,
                                        PROTOCOL,
                                        CHECKSUM,
                                        SRC_PORT,
                                        DEST_PORT,
                                        seq_num,
                                        ack_num,
                                        WINDOW,
                                        payload_len )

        self.send(header)



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