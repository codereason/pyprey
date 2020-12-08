import configparser
import sys
sys.path.append(__file__)

class Config(object):
    def __init__(self,config_path='config.ini'):

        self.config_path = config_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_path)
        self.conf_dict = {}
    def get_configs(self):
        ''' return a dict of configs  key-value pair'''
        # for section in self.conf.sections():
        for section in self.conf.sections():
            self.conf_dict[section] = {i[0]:i[1] for i in self.conf.items(section)}
            
        return self.conf_dict

# if __name__ == "__main__":
# cf = Config()
# get_cf = cf.get_configs()
# print(get_cf)
    # print(['nlp']['STOP_WORDS_PATH'])

if __name__ == "__main__":
    cf = Config()
    get_cf = cf.get_configs()
    print(get_cf)
