import json
import logging
logging.basicConfig(level=logging.INFO)
import os


def read_order_data_json(file_name):
    # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # path_dir = curpath + "/Config/"
    # current_path = path_dir + file_name

    root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    current_path = root_path + "/app/Kit/Courier/Config/" + file_name
    with open(current_path, "r", encoding='utf-8') as f:
        data = json.load(f)
        logging.info("填单接口,请求数据参数,读取结果是：")
        logging.info(data)
        return data
