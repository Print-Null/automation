import json


class BaseApi:
    @classmethod
    def format(cls, r):
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
