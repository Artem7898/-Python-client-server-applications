from utils import *


presence_msg = {"action": "presence", "time": timestr, "type": "status",
                "user": {"account_name": "Somebody", "status": "Hello there!"}}



def parsing_server_msg(s, server_message):
    if 'action' in server_message.keys():
        if server_message['action'] == 'probe':
            send_msg(s, presence_msg)
            return server_message, 'action'


    elif 'response' in server_message.keys():
        if server_message['alert']:
            server_response = {'response': server_message['response'], 'time': server_message['time'],
                               'contents': server_message['alert'], 'type': 'alert'}
        elif server_message['error']:
            server_response = {'response': server_message['response'], 'time': server_message['time'],
                               'contents': server_message['error'], 'type': 'error'}
        else:
            server_response = {'response': 'unknown', 'time': timestr,
                               'contents': [server_message], 'type': 'unknown'}
        return server_response, 'response'


    else:
        server_response = {'response': 'unknown', 'time': timestr,
                           'contents': [server_message], 'type': 'unknown'}
        return server_response, 'response'

