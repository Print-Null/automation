import logging
import requests

from app.Kit.Util.common_data import Common_data


class Ms_Login():
    logging.basicConfig(level=logging.INFO)
    def ms_login(self):
        comm = Common_data()
        # host = read_common("ms_host")
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/auth/signin"
        header = {
            "Content-Type": "application/json"
        }

        # user = read_common("ms_login_user")
        user = comm.each_parameter("ms_login_user")
        # pwd = read_common("ms_login_pwd")
        pwd = comm.each_parameter("ms_login_pwd")
        data ={"login": user, "password": pwd}
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        session = resp.json()["data"]["session_id"]
        logging.info(session)
        comm.write_parameter_to_redis("ms_session", str(session))
        return resp.json()

