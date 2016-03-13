
'''  UDP_client.py                                     
Use the better name for this module: upper_case_client_UDP   
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT NAME                                 
  COURSE NAME and SEMESTER                    
  DATE                                         
  This module will <blah, blah, blah>              
'''

from socket import *

# STUDENTS - change 'servername' to the domain name of your server or to
# its IP address.
server_name = 'servername'

# STUDENTS - Set this to the port number your server uses!        
server_port = 12000

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
