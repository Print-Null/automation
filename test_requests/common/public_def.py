import ast
import hashlib
import datetime
from interface_aotumation.utils.redisbase import RedisBase
from interface_aotumation.common.readconfig import ReadConfig


def create_sign(**kwargs):
    parameter = kwargs.get("parameter") if kwargs.get("parameter") else None
    # 拿到配置文件中对应环境的key
    redisObj = RedisBase()
    env = redisObj.get("runenv_py")
    read_config_object = ReadConfig()
    if env is False:
        env = "trunk"
    else:
        env = redisObj.get("runenv_py")
    key = read_config_object.get_config(env, "key")

    parameter_dict = ast.literal_eval(parameter)
    argument_list = []
    for k, v in parameter_dict.items():
        if v != "" and k != "sign":
            argument_list.append(k)
    argument_list.sort()
    sha_string_list = []
    for i in argument_list:
        sha_string_list.append(i)
        sha_string_list.append("=")
        sha_string_list.append(str(parameter_dict[i]))
        sha_string_list.append("&")
    sha_string = "".join(sha_string_list)
    string_sign_temp = sha_string + "key=" + key
    sha256 = hashlib.sha256()
    sha256.update(string_sign_temp.encode("utf-8"))
    sign = sha256.hexdigest().upper()
    return sign


def if_weekend(day_str, separator = ""):
    """
    if a day is weekend
    :param day_str: string of a day
    :param separator: separator of year, month and day, default is empty
    :return: True: is weekend; False: not weekend
    """
    spec = "%Y" + separator + "%m" + separator + "%d"
    day = datetime.datetime.strptime(day_str, spec).date()
    # Monday == 0 ... Sunday == 6
    if day.weekday() in [5, 6]:
        return True
    else:
        return False
