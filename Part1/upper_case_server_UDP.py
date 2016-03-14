'''
  Gary Sidoti and Vincent Nguyen
  CISC450 - Spring 2016                    
  4/8/16                                         
  This module will <blah, blah, blah>              
'''

from socket import *

# STUDENTS: randomize this port number (ideally 49152- 65535, but 1024-65535 will work)
# done
server_port = 52832

# create UDP listening socket and bind it to the server port
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The Upper Case Server is running over UDP and ready to receive ... ')

while True:
    # read client's message and client's IP address and port number (1KB max)
    # this is a blocking call by default
    message, client_address = server_socket.recvfrom(1024)

    # output the sentence received from client (converted to a string)
    print('Received from Client over UDP: ', message.decode())
	
    # convert the sentence to upper case
    # Note that sentence is still a bytes object rather than a string, but
    # upper() also works for byte objects
    modified_message = message.upper()
	
    # send back modified sentence over UDP
    # Note that this requirest the client's address info
    server_socket.sendto(modified_message, client_address)
 
    # output message sent back to client (converted to a string)
    print('Sent back to Client over UDP: ', modified_message.decode())
