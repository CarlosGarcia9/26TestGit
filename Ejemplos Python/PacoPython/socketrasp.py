import socket

def main():
	#my machine"
	host = '127.0.0.1'
	port=5000

	#Create a new socket
	s=socket.socket()

	#bind a socket to a port
	s.bind((host,port))

	#listening for conexion
	s.listen(1) #1 conexion
	c, addr =s.accept() #accept de conexion
	print("Connection from: ", str(addr))
	while True:
		data=c.recv(1024) #recive maxiumum 1024
		if not data:
			break
		print("from connected user: " + str(data))


