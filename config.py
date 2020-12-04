import configparser
import sys

sys.setdefaultencoding("utf-8")
class Config(object):
    def __init__(self,config_path='pyprey_config.ini'):
        self.config_path = config_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_path)
    def configs(self):
        ''' return a dict of configs  key-value pair'''
        configs = {}
        self.conf
        return configs
