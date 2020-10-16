import configparser
import os


def write_ini(filename,section,option,Values,mode):
    root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    pack_number_path = root_path + "/app/backyard/test_backstage/conf/"+filename+".ini"
    cf = configparser.ConfigParser()
    cf.add_section(section)
    cf.set(section, option=option, value=str(Values))
    with open(pack_number_path, mode) as f:
        cf.write(f)