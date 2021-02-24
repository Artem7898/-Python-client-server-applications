from utils import *
from loguru import logger

# Логирование с помощью библиотеке loguru:

logger.add("server_func_debug.log.txt", format="{time} {level} {message}", level="DEBUG", rotation="10:00", compression="zip")


presence_request = {'action': 'probe', 'time': timestr}

response_100 = {'response': 100, 'time': timestr,
                'alert': 'Welcome to our server'}

response_400 = {'response': 400, 'time': timestr,
                'error': 'Bad request/JSON object'}


def handling_client_msg(client_msg, addr):
    if client_msg['action'] == 'presence':
        if client_msg['user']['account_name']:
            client_data = {'client': {'address': addr, 'account_name': client_msg['user']['account_name']},
                           'message': {'text': client_msg['user']['status'], 'type': client_msg['type'],
                                       'time': client_msg['time']}}
            return response_100
        else:
            return response_400
    else:
        return response_400

    return client_msg, addr


logger.debug("handling_client_msg(dedug)!")
logger.info("handling_client_msg(dedug)!")
logger.error("handling_client_msg(dedug)!")
logger.warning("handling_client_msg(dedug)!")
logger.critical("handling_client_msg(dedug)!")


@logger.catch
def main():
    handling_client_msg(1 / 0)


main()
