import binascii
import socket as syssock
import struct
import sys

# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

def init(UDPportTx, UDPportRx):   # initialize your UDP socket here
	#Initialize UDP socket
	global MAIN_SOCKET
	MAIN_SOCKET = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)

	# UDP Port
	global RECV_PORT, SEND_PORT
	RECV_PORT = UDPportTx
	SEND_PORT = UDPportRx

    # Header Default Structure & Values
	global PKT_HEADER_DATA, PKT_HEADER_FMT, HEADER_LEN, VERSION, OPT_PTR, PROTOCOL, SRC_PORT, DEST_PORT, WINDOW, CHECKSUM
	PKT_HEADER_FMT = '!BBBBHHLLQQLL'
	PKT_HEADER_DATA = struct.Struct(PKT_HEADER_FMT)
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
    
	def __init__(self):
		pass

	def bind(self, address):
	    MAIN_SOCKET.bind(address)

	def connect(self, address):  # fill in your code here
		# Create the SYN header
		# Send the SYN packet A
		# Start timer
		# recv SYN ACK B
		# send ACK C
		# If there is error, send header again


	    # Connect to server address
		MAIN_SOCKET.connect(address)

	    # Create SYN header
		seq_num = 19 # random number
		ack_num = seq_num + 1
		payload_len = 0

		syn_header = PKT_HEADER_DATA.pack(	VERSION,
											SYN,
											OPT_PTR,
											PROTOCOL,
											HEADER_LEN,
											CHECKSUM,
											SRC_PORT,
											DEST_PORT,
											seq_num,
											ack_num,
											WINDOW,
											payload_len )

		ack_header = PKT_HEADER_DATA.pack(	VERSION,
											ACK,
											OPT_PTR,
											PROTOCOL,
											HEADER_LEN,
											CHECKSUM,
											SRC_PORT,
											DEST_PORT,
											seq_num+1,
											ack_num+1,
											WINDOW,
											payload_len ) # TODO

	    # Set timeout to 0.2 seconds and send SYN packet A
		MAIN_SOCKET.settimeout(0.2)
		MAIN_SOCKET.send(syn_header)
		for i in range(0, 10):
			while True:
				try:
					# Receive SYN ACK packet B
					data, server = MAIN_SOCKET.recvfrom(HEADER_LEN)
					print('Worked: %s' % (data))
					# Send ACK packet C
					MAIN_SOCKET.send(ack_header)
				except syssock.timeout:
					# Resend on timeout
					print('REQUEST TIMED OUT, RESENDING...')
					continue
				break


	def listen(self, backlog):
	    return

	def accept(self):
		# recv SYN A
		# send SYN ACK B
		# ACK C

		# recv SYN A
		data = None
		while (data is None):
			(data, address) = MAIN_SOCKET.recvfrom(HEADER_LEN)
	    
	    # Check is valid SYN
		recv_header = struct.unpack(PKT_HEADER_FMT, data)

		if (recv_header[1] != SYN):
			print("Error: Received packet is not SYN")

		# Create SYN header
		seq_num = 29 # random number
		ack_num = recv_header[8] + 1 # client seq_num + 1
		payload_len = 0		

		# Send SYN ACK B
		syn_header = PKT_HEADER_DATA.pack(	VERSION,
											SYN | ACK,
											OPT_PTR,
											PROTOCOL,
											HEADER_LEN,
											CHECKSUM,
											SRC_PORT,
											DEST_PORT,
											seq_num,
											ack_num,
											WINDOW,
											payload_len)

		MAIN_SOCKET2 = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
		MAIN_SOCKET2.bind((address[0],RECV_PORT))
		bytessent = 0
		while (bytessent != HEADER_LEN):
			bytessent += MAIN_SOCKET2.send(syn_header)

		return (MAIN_SOCKET2, address)

	def close(self):   # fill in your code here 
	    return 

	def send(self, buffer):
		# Create header
		# Send data
		# Start timer
		# If timeout, send same packet again
	    bytessent = 0
	    return bytessent 

	def recv(self, nbytes):
		# Packets recv
		# Send right ACK
	    bytesreceived = 0
	    return bytesreceived