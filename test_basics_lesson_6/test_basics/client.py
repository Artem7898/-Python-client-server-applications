from client_functions import *
from utils import *
from socket import *
from sys import argv


addr, port = get_addr_port(argv, 'configs_client.yaml')

s = socket(AF_INET, SOCK_STREAM)
s.connect((addr, int(port)))

server_responses = []

while True:
    msg_in = s.recv(10000)
    if msg_in:
        server_message = get_msg(msg_in)

        server_response, msg_type = parsing_server_msg(s, server_message)

        if msg_type == 'response':
            server_responses.append(server_response)
            print(server_response)
