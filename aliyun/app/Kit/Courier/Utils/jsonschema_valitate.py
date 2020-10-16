import json
import logging
from jsonschema import validate
logging.basicConfig(level=logging.INFO)
import os


def Validate_jsonschema(response_result, schema_file_name):
    # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # path_dir = curpath + "/jsonschema_validate/"

    root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    path_dir = root_path + "/app/Kit/Courier/jsonschema_validate/"

    current_path = path_dir + schema_file_name
    with open(current_path, "r", encoding='utf-8') as f:
        shcema = json.load(f)
        res = validate(instance=response_result, schema=shcema)
        logging.info("jsonschema验证结果是： " + str(res))
        return res

