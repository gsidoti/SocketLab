'''
  Gary Sidoti and Vincent Nguyen
  CISC450 - Spring 2016                    
  4/8/16                                         
  This module will <blah, blah, blah>              
'''

from socket import *

# STUDENTS - change 'servername' to the domain name of your server or to
# its IP address.
server_name = '100.34.188.112'

# STUDENTS - Set this to the port number your server uses!        
server_port = 52832

# create UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# get user's input
message = input('Input lowercase sentence: ')

# send the user's input to server (converted to bytes)
client_socket.sendto(message.encode(), (server_name, server_port))

# output what was sent to the server
print ('Sent to Upper Case Server over UDP: ', message)

# receive modified sentence from server (1KB max)
# this is a blocking call by default
modified_message, server_address = client_socket.recvfrom(1024)

# output modified sentence (converted to bytes)
print ('Received from Server over UDP: ', modified_message.decode())

# close the UDP socket
client_socket.close()
