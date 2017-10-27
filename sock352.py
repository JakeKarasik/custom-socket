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
	
	# Save recv port for server binding
	global portRx, portTx
	portRx = int(UDPportRx)
	portTx = int(UDPportTx)

    # Header Default Structure & Values
	global PKT_HEADER_DATA, PKT_HEADER_FMT, HEADER_LEN, VERSION, OPT_PTR, PROTOCOL, SRC_PORT, DEST_PORT, WINDOW, CHECKSUM
	PKT_HEADER_FMT = '!BBBBHHLLQQLL'
	PKT_HEADER_DATA = struct.Struct(PKT_HEADER_FMT)
	HEADER_LEN = struct.calcsize(PKT_HEADER_FMT)
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

	# Connection is set?
	global CONNECT_SET
	CONNECTION_SET = False

class socket:
    
	def __init__(self):
		pass

	def bind(self, address):
		MAIN_SOCKET.bind(('',portRx))

	def connect(self, address):
		# Create the SYN header
		# Send the SYN packet A
		# Start timer
		# recv SYN ACK B
		# send ACK C
		# If there is error, send header again

	    # Connect to server address
		MAIN_SOCKET.connect((address[0], portTx))

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

	    # Set timeout to 0.2 seconds
		MAIN_SOCKET.settimeout(0.2)

		done = False
		response = []
		bytesreceived = 0

		# Attempt to resend up to 5 times
		for i in range(0, 5):

			if (done):
				break

			# Attempt to send SYN packet A
			try:
				MAIN_SOCKET.sendall(syn_header)
			except syssock.error: 
				print("Failed to send SYN packet A")
				continue

			while not done:
				try:
					# Receive SYN ACK packet B
					(data, address) = MAIN_SOCKET.recvfrom(HEADER_LEN)
					
					# Append packet to response array
					response.append(data)

					# Add size of packet to bytes received
					bytesreceived += len(data)

					# Check if done receiving
					if (bytesreceived == HEADER_LEN):
						done = True
						break
				except syssock.timeout:
					# Resend on timeout
					print("Request timed out, resending")
					i += 1
					break
				except syssock.error:
					print("Failed to send/receive, trying again")
					i += 1
					break

		# Check if header successfully received
		if (bytesreceived != HEADER_LEN):
			print("Failed to receive.")
			return

		# Put packets together
		response = "".join(response)
		response_as_struct = struct.unpack(PKT_HEADER_FMT,response)

		print(response_as_struct)

		# Check correct response
		if (response_as_struct[1] != SYN | ACK and response_as_struct[1] != RES):
			print("Error: Received packet is not SYN-ACK or RES")

		# Notify RESET flag received
		if (response_as_struct[1] == RES):
			print("Notice: RESET flag received")

		# Create SYN-ACK header
		new_seq_num = response_as_struct[9]
		new_ack_num = response_as_struct[8] + 1

		ack_header = PKT_HEADER_DATA.pack(	VERSION,
											SYN | ACK,
											OPT_PTR,
											PROTOCOL,
											HEADER_LEN,
											CHECKSUM,
											SRC_PORT,
											DEST_PORT,
											new_seq_num,
											new_ack_num,
											WINDOW,
											payload_len )

		# Attempt to send ACK packet C
		try:
			MAIN_SOCKET.sendall(ack_header)
		except syssock.error: 
			print("Failed to send ACK packet C")


	def listen(self, backlog):
	    return

	def accept(self):
		# recv SYN A
		# send SYN ACK B
		# ACK C
		global CONNECTION_SET

		# recv SYN A
		(data, address) = MAIN_SOCKET.recvfrom(HEADER_LEN)

	    # Check is valid SYN
		recv_header = struct.unpack(PKT_HEADER_FMT, data)

		print(recv_header)

		if (recv_header[1] != SYN):
			print("Error: Received packet is not SYN")

		# Create SYN header
		seq_num = 29 # random number
		ack_num = recv_header[8] + 1 # client seq_num + 1
		payload_len = 0
		
		# If there is an existing connection, the RESET flag is set. 
		flags = SYN | ACK if not CONNECT_SET else RES

		# Create SYN ACK B
		syn_header = PKT_HEADER_DATA.pack(	VERSION,
											flags,
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

		try:
			MAIN_SOCKET.sendto(syn_header, address)
		except syssock.error: 
			print("Failed to send SYN ACK B")

		# recv SYN-ACK C
		(data, address) = MAIN_SOCKET.recvfrom(HEADER_LEN)

		print(struct.unpack(PKT_HEADER_FMT, data))

		# Mark connection as set
		CONNECTION_SET = True

		return (MAIN_SOCKET, address)

	def close(self):   # fill in your code here 
		global CONNECTION_SET
		CONNECTION_SET = False
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