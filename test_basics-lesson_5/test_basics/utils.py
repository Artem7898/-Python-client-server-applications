import yaml
import json
import time
from loguru import logger

# Логирование с помощью библиотеке loguru:

logger.add("utils_debug.log.txt", format="{time} {level} {message}", level="DEBUG", rotation="10:00", compression="zip")


def get_addr_port(argv, config_file):
    if len(argv) == 5:
        port = argv[4]
        addr = argv[2]
    elif len(argv) == 3:
        if argv[1] == '-p':
            port = argv[2]
            addr = parse_configs(config_file)[0]
        elif argv[1] == '-a':
            addr = argv[2]
            port = parse_configs(config_file)[1]
    else:
        port = parse_configs(config_file)[1]
        addr = parse_configs(config_file)[0]

    return addr, port



def parse_configs(file_name):
    with open(file_name, encoding='utf-8') as y:
        y_content = yaml.load(y, Loader=yaml.Loader)
    return y_content['addr'], y_content['port']



def get_msg(msg_in):
    json_in = json.loads(msg_in)
    return json_in


def send_msg(destination_host, msg):
    g = json.dumps(msg)
    destination_host.send(g.encode('utf-8'))


timestr = time.ctime(time.time()) + "\n"

logger.debug("get_addr_port(dedug)!")
logger.info("get_addr_port(dedug)!")
logger.error("get_addr_port(dedug)!")

logger.debug("parse_configs(dedug)!")
logger.info("parse_configs(dedug)!")
logger.error("parse_configs(dedug)!")

logger.debug("send_msg(dedug)!")
logger.info("send_msg(dedug)!")
logger.error("send_msg(dedug)!")



