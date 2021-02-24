from server_functions import *
from utils import *
from socket import *
from sys import argv


addr, port = get_addr_port(argv, 'configs_server.yaml')

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', int(port)))
s.listen(3)


while True:
    client, addr = s.accept()

    send_msg(client, presence_request)

    msg_in = client.recv(10000)
    client_msg = get_msg(msg_in)

    response = handling_client_msg(client_msg, addr)
    print(response)

    send_msg(client, response)

    client.close()


