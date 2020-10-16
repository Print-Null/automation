import re

import requests

#获取html页面中的请求参数
def get_html():

    # url = "http://bi.test.fe.com/cs/ssjudge?lang= zh-CN&auth= 9ebc42d3de7862fd5907eda6e49eabc7&fbid= 22521&time= 1592812086&page= 1&pagesize= 100&keyword= &source= &state= &tab= 1&startTime= 1592758800&endTime= 1592845199&area= &vip_type= &taskStartTime= &taskEndTime= &handleStartTime= &handleEndTime="
    url = "http://bi.test.fe.com/cs/ssjudge"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN",
        "BI-PLATFORM": "",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "_ga=GA1.2.1105378886.1568691037; lang=zh-CN; PHPSESSID=847hbbddo1m97n2t59r2hnvp83; _gid=GA1.2.424642011.1592792291; _gat_gtag_UA_145656102_1=1; PHPSESSID=mpem9i25ma43b917fio2jftcit; lang=zh-CN",
        "Host": "bi.test.fe.com"
    }
    '''
    Cookie  这里面的PHPSESSID 从哪里来的？
    '''
    # response = requests.request("GET", url, headers=headers, data=payload)
    response = requests.get(url=url, headers=headers)
    # print(response.text.encode('utf8'))
    s = response.text.encode("utf-8")
    html_utf8 = str(s, encoding="utf-8")
    # print(type(html_utf8))
    var_list = re.findall('<iframe[^>]+src="([^"]+)"', html_utf8)
    # print(var_list)
    uu = str(var_list).split("?")[1]
    # print(uu)
    url_data = uu.split("'")[0]
    # print(url_data)
    lang = url_data.split("&")
    # print(lang[0])
    # print(lang[1])
    # print(lang[2])
    # print(lang[3])


    return lang[0],lang[1],lang[2],lang[3]

if __name__ == '__main__':
    get_html()