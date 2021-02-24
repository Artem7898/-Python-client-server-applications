import unittest
from utils import *
from client_functions import *
from server_functions import *

class TestGettingConfigs(unittest.TestCase):
    default_addr_server = ''
    default_addr_client = '127.0.0.1'
    port = 7777
    script_name_server = 'server.py'
    script_name_client = 'client.py'
    config_source_server = 'configs_server.yaml'
    config_source_client = 'configs_client.yaml'
    result_server = ('', 7777)
    result_client = ('127.0.0.1', 7777)


    def testParseConfigsServer(self):
        self.assertEqual(parse_configs(self.config_source_server), self.result_server)

    def testParseConfigsClient(self):
        self.assertEqual(parse_configs(self.config_source_client), self.result_client)


    def testGetFullParamsServer(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-a', self.default_addr_server, '-p', self.port],
                                       self.config_source_server),
                         self.result_server)

    def testGetFullParamsClient(self):
        self.assertEqual(get_addr_port([self.script_name_client, '-a', self.default_addr_client, '-p', self.port],
                                       self.config_source_server),
                         self.result_client)
    

    def testGetAddrServer(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-a', self.default_addr_client],
                                       self.config_source_server),
                         self.result_client)

    def testGetAddrClient(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-a', self.default_addr_client],
                                       self.config_source_server),
                         self.result_client)
    
    def testGetPortServer(self):
        self.assertEqual(get_addr_port([self.script_name_server, '-p', self.port], self.config_source_server),
                         self.result_server)

    def testGetPortClient(self):
        self.assertEqual(get_addr_port([self.script_name_client, '-p', self.port], self.config_source_client),
                         self.result_client)

    
    def testGetScriptServer(self):
        self.assertEqual(get_addr_port([self.script_name_server], self.config_source_server), self.result_server)

    def testGetScriptClient(self):
        self.assertEqual(get_addr_port([self.script_name_client], self.config_source_client), self.result_client)





if __name__ == '__main__':
    unittest.main()


