import configparser
import os


def read_ini(filename,sections,option):
    cf = configparser.ConfigParser()
    root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    path_common = root_path + "/app/backyard/test_backstage/conf/"+filename+".ini"
    print(path_common)
    cf.read(path_common, encoding="UTF-8")
    get_common = cf.get(sections, option)
    return get_common