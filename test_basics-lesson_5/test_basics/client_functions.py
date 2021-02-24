from utils import *
from loguru import logger

# Логирование с помощью библиотеке loguru:

logger.add("client_func_debug.log.txt", format="{time} {level} {message}", level="DEBUG", rotation="10:00", compression="zip")

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


logger.debug("def parsing_server_msg(dedug)!")
logger.info("def parsing_server_msg(dedug)!")
logger.error("def parsing_server_msg(dedug)!")
logger.warning("def parsing_server_msg(dedug)!")
logger.critical("def parsing_server_msg(dedug)!")

logger.debug("presence_msg(dedug)!")
logger.info("presence_msg(dedug)!")
logger.error("presence_msg(dedug)!")
logger.warning("presence_msg(dedug)!")
logger.critical("presence_msg(dedug)!")


