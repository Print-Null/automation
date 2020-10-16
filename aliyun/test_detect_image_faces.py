import json
import pytest
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkimm.request.v20170906.DetectImageFacesRequest import DetectImageFacesRequest


# 参数值测试：调用阿里云python-SDK的实现，测试内容和方法二类同
@pytest.mark.parametrize("image_uri,project", {
    ("", "detect-image-faces"),  # 必须参数ImageUri为空
    ("oss://detect-image-faces/liuyifei.jpg", ""),  # 必须参数Project为空
    ("oss://detect-image-faces/wrong/太阳.jpg", "detect-image-faces"),  # 必须参数ImageUri地址错误
    ("oss://detect-image-faces/liuyifei.jpg", "detect-image-faces-wrong"),  # 必须参数Project名称错误
    ("oss://detect-image-faces/liuyifei.jpg", "detect-image-faces"),  # 传入jpg的真实人物照片
    ("oss://detect-image-faces/凡人修仙.png", "detect-image-faces"),  # 传入卡通人物的png照片
    ("oss://detect-image-faces/face.psd", "detect-image-faces"),  # 传入PSD格式的人脸照片
    ("oss://detect-image-faces/face.tif", "detect-image-faces"),  # 传入TIF格式的人脸照片
    ("oss://detect-image-faces/face.abr", "detect-image-faces"),  # 传入ABR格式的人脸照片
    ("oss://detect-image-faces/face.atn", "detect-image-faces"),  # 传入ATN格式的人脸照片
    ("oss://detect-image-faces/face.ai", "detect-image-faces"),  # 传入AI格式的人脸照片
    ("oss://detect-image-faces/face.cdr", "detect-image-faces"),  # 传入CDR格式的人脸照片
    ("oss://detect-image-faces/face.eps", "detect-image-faces"),  # 传入EPS格式的人脸照片
    ("oss://detect-image-faces/太阳.jpg", "detect-image-faces"),  # 传入非人物照片
    ("oss://detect-image-faces/背影.jpg", "detect-image-faces"),  # 传入只有背影的图片
    ("oss://detect-image-faces/半边脸.jpg", "detect-image-faces"),  # 传入只有半张脸的图片
    ("oss://detect-image-faces/半边脸马赛克.jpg", "detect-image-faces"),  # 传入脸部带有马赛克的图片
    ("oss://detect-image-faces/猫咪.jpg", "detect-image-faces"),  # 传入非人脸照片
    ("oss://detect-image-faces/test.txt", "detect-image-faces")  # 传入非图片格式的文件，此处以txt为例
})
def test_detect_image_faces(image_uri, project):
    client = AcsClient('LTAI4GHFNSouZMtHSXtdppEg', 'ldcDuhTvfGN99YnEM0gkIddheQai4r', 'cn-beijing')
    req = DetectImageFacesRequest()
    req.set_Project(project)
    req.set_ImageUri(image_uri)
    response = client.do_action_with_exception(req)
    print(json.dumps(json.loads(response), indent=2))

# 接口请求参数测试：使用requests库自己拼接请求实现(签名未搞定，所以真实的跑不起来)
class TestDetectImageFaces:
    public_params = {"format": "JSON",
                     "Version": "2017-09-06",
                     "AccessKeyId": "AccessKeyId",
                     "Signature": "Signature",
                     "SignatureMethod": "SignatureMethod",
                     "Timestamp": "Timestamp",
                     "SignatureVersion": "SignatureVersion",
                     "SignatureNonce": "SignatureNonce"}
    base_url = "https://imm.cn-shanghai.aliyuncs.com"

    # 不考虑测试公共参数

    # case1：测试请求参数"Action"为空
    @pytest.mark.action
    def test_action_none(self):
        params = {"Action": "",
                  "Project": "Project",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case2：测试请求参数"Action"不为string，此处只以传入int数字为例
    @pytest.mark.action
    def test_action_not_string(self):
        params = {"Action": 123,
                  "Project": "Project",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case3：测试请求参数"Action"为错误的action
    @pytest.mark.action
    def test_action_wrong(self):
        params = {"Action": "abc",
                  "Project": "Project",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case4：测试请求参数没有"Action"
    @pytest.mark.action
    def test_no_action(self):
        params = {"Project": "Project",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case5：测试请求参数"Project"为空
    @pytest.mark.project
    def test_project_none(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case6：测试请求参数"Project"不为string，此处只以传入int数字为例
    @pytest.mark.project
    def test_project_not_string(self):
        params = {"Action": "DetectImageFaces",
                  "Project": 555,
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case7：测试请求参数"Project"为错误的project
    @pytest.mark.project
    def test_project_wrong(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "wrong-project",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case8：测试不传入必须参数"Project"
    @pytest.mark.project
    def test_no_project(self):
        params = {"Action": "DetectImageFaces",
                  "ImageUri": "oss://bucket/object"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case9：测试请求参数"ImageUri"为空
    @pytest.mark.imageuri
    def test_imageuri_none(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "Project",
                  "ImageUri": ""}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case10：测试请求参数"ImageUri"不为string，此处只以传入布尔类型True为例
    @pytest.mark.imageuri
    def test_imageuri_not_string(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "Project",
                  "ImageUri": True}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case11：测试请求参数"ImageUri"为错误的ImageUri
    @pytest.mark.imageuri
    def test_imageuri_wrong(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "Project",
                  "ImageUri": "wrong-oss://imm-test/testcases/test.jpg"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case12：测试不传入必须参数"ImageUri"
    @pytest.mark.imageuri
    def test_no_imageuri(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "Project"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case13：测试"ImageUri"传入不同格式的图片，比如jpg|png|bmp|tif|gif|pcx|tga|exif|fpx|svg等等，
    # case14：测试传入超大图片
    @pytest.mark.imageuri
    def test_imageuri_wrong(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "Project",
                  "ImageUri": "oss://imm-test/testcases/test.jpg"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case15：测试"ImageUri"传入其他格式的文件，比如txt|docx|excel|mp4|pdf等等，这里只以txt为例
    @pytest.mark.imageuri
    def test_imageuri_wrong(self):
        params = {"Action": "DetectImageFaces",
                  "Project": "Project",
                  "ImageUri": "oss://imm-test/testcases/test.txt"}
        params.update(self.public_params)
        r = requests.post(url=self.base_url,
                          params=params)
        return r.json()

    # case16：测试参数传入的先后顺序，比如"ImageUri"参数在"Project"参数前面，"Project"参数在"Action"前面等等
    # case17：还可以考虑输入超长参数值的测试，比如Project或者ImageUri的参数值输入几十个几百个字符
    # case18：还可以考虑参数值里面带有特殊符号或者中文的测试
