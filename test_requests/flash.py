import json

import requests

# r = requests.get(url="http://www-training.flashexpress.com/zh/")
# res = json.dumps(r.json(), ensure_ascii=False)
# print(res)
header = {#"Connection": "keep-alive",
          #"Accept": r"*/*",
          #"X-Requested-With": "XMLHttpRequest",
          #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
          #"Accept-Encoding": "gzip, deflate",
          #"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
          "Accept-Language": "zh-CN",
          #"Content-Length": "9"
          }
cookie = {"ga": "GA1.2.7487673.1592279367",
          "gid": "GA1.2.54014882.1592279367",
          "PHPSESSID": "jlod2q3p40mqjcaq6qfug8ltdg",
          "lang": "en",
          "gat_gtag_UA_123075178_1": "1"}
params = {"account": "BA0020", "pwd": "648576"}
r = requests.post(url="http://www-training.flashexpress.com", headers=header, cookies=cookie,
                  params=params)

res = json.dumps(r.json(), ensure_ascii=False)
print(res)
