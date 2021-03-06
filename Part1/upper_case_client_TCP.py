'''
  Gary Sidoti and Vincent Nguyen
  CISC450 - Spring 2016                    
  4/8/16                                         
  This module will <Send a sentence to the server and recieve a uppercase response>              
'''

from socket import *

# STUDENTS - change 'servername' to the domain name of your server or to
# its IP address.
server_name = '100.34.188.112'

# STUDENTS - Set this to the port number your server uses!        
server_port = 52832

# create TCP socket for connecting to remote server.
client_socket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
client_socket.connect((server_name,server_port))

# get user's input
sentence = input('Input lowercase sentence: ')

# send the user's input to server (must convert to bytes)
client_socket.send(sentence.encode())

#output what was sent to the server
print ('Sent to Upper Case Server over TCP: ', sentence)

# get modified line back from server (1KB max)
# This is a blocking call by default
modified_sentence = client_socket.recv(1024)

# output the modified user's line (converted to a string)
print ('Received from Upper Case Server over TCP: ', modified_sentence.decode())

# close the TCP connection
client_socket.close()