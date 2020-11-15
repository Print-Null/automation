import json
import requests
from locust import HttpUser, TaskSet, task


class CeShiRen(TaskSet):

    @task(1)
    def ceshiren(self):
        header = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "ceshiren.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "same-origin",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1"
        }
        req = self.client.get(url="https://www.ceshiren.com", headers=header, verify=False)
        print(req.status_code)
        if req.status_code == 200:
            print("success")
        else:
            print("failed")


class WebSitUser(HttpUser):
    task_create = [CeShiRen]
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒


if __name__ == "__main__":
    import os

    os.system("locust -f locust_study.py --csv=ceshiren --headless -u500 -r10 -t10s --host=https://www.ceshiren.com")

# --web-host=127.0.0.1 指定webUI的host
