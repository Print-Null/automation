import json

import requests
import yaml


class BaseApi:
    data = {}

    @classmethod
    def format(cls, r):
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))

    @classmethod
    def load_yaml(cls, path):
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def api_load(self, path):
        return self.load_yaml(path)

    # 使用数据驱动模拟requests请求
    def api_send(self, req: dict):
        # req["params"]["access_token"] = self.get_token(self.secret)
        r = requests.request(req["method"], url=req["url"], params=req["params"], json=req["json"])
        self.format(r)
        return r.json()
