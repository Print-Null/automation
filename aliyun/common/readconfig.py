import configparser
import logging
import os


class ReadConfig:
    """定义一个读取配置文件的类"""
    logging.basicConfig(level = logging.INFO)

    def __init__(self, filepath = None):
        root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        configpath = os.path.join(root_path, "env.ini")
        configpath1 = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "conf/conf.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath, encoding = "utf-8")
        self.cf.read(configpath1, encoding = "utf-8")

    def get_config(self, confname, param):
        value = self.cf.get(confname, param)
        return value
