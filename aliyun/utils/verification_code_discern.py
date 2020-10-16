# 创建AipOcr
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '20536298'
API_KEY = 'oix9BQ9HhnaVtxcTXg64HmjP'
SECRET_KEY = 'byLq3f82MqPjtHafhmLctGOQaDgOkymG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 文字识别高精度版本

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('1.png')

""" 调用通用文字识别（高精度版） """
client.basicAccurate(image);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
a = client.basicAccurate(image, options)
print(a)
