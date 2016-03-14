'''
  Gary Sidoti and Vincent Nguyen
  CISC450 - Spring 2016                    
  4/8/16                                         
  This module will <Setup a connection and respond when given a sentence from the client>              
'''

from socket import *

# STUDENTS: randomize this port number (ideally 49152- 65535, but 1024-65535 will work)
server_port = 52832

# create TCP listening socket and bind it to the server port
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))

# listen for incoming TCP requests
server_socket.listen(1)
print ('The Upper Case Server is running over TCP and listening ... ')

while True:
    # server accepts incoming request; new socket created on return
    # this is a blocking call by default
    connection_socket, addr = server_socket.accept()
     
    # read bytes from socket (sent by client)
    # this is a blocking call by default
    sentence = connection_socket.recv(1024)

    # output the sentence received from client (converted to a string)
    print ('Received From Client over TCP: ', sentence.decode())
	 
    # convert the sentence to upper case
    # Note that sentence is still a bytes object rather than a string, but
    # upper() also works for byte objects
    uppercase_sentence = sentence.upper()
	 
    # send back modified sentence over the TCP connection
    connection_socket.send(uppercase_sentence)

    # output sentence sent back to client (converted to a string)
    print ('Sent back to Client over TCP: ', uppercase_sentence.decode())
	 
    # close the TCP connection; the listening socket continues listening
    connection_socket.close()
