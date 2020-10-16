import json
import os


def read_json_file(file_name):
    root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    pack_number_path = root_path + "/app/backyard/test_backstage/conf/"+file_name+".json"
    with open(pack_number_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data