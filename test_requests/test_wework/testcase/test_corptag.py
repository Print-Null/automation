import pytest
from jsonpath import jsonpath
from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.corptag import CorpTag


class TestCorpTag:
    corptag = None
    data = BaseApi().load_yaml(r"E:\MyProjects\test_requests\test_wework\testcase\test_tag.data.yaml")

    @classmethod
    def setup(cls):
        cls.corptag = CorpTag()
        cls.reset()

    def test_get_corptag(self):
        r = self.corptag.get_corptag()
        assert r["errcode"] == 0
        print("\n获取企业标签的用例通过")

    def test_get_api(self):
        r = self.corptag.get_api()
        assert r["errcode"] == 0
        print("\n通过数据驱动获取企业标签通过")

    def test_add_corptag(self):
        r = self.corptag.add_corptag("tag2")
        assert r["errcode"] == 0
        print("\n增加企业标签的用例通过")

    @pytest.mark.parametrize("name", ["tag2", "tag3", "tag4"])
    def test_add_api(self, name):
        r = self.corptag.add_api(name)
        assert r["errcode"] == 0
        print("\n通过数据驱动添加企业标签通过")

    def test_update_corptag(self):
        r = self.corptag.add_api("edit")
        tag_id = jsonpath(r, f"$..tag[?(@.name=='edit')]")[0]["id"]
        r = self.corptag.update_corptag(tag_id, "new_edit")
        assert r["errcode"] == 0
        self.corptag.get_api()
        self.corptag.delete_api([tag_id])

    # # 参数化
    # @pytest.mark.parametrize("name", ["tag2", "tag3", "tag4"])
    @pytest.mark.parametrize("name", data["test_delete"])
    def test_delete_corptag(self, name):
        self.corptag.get_corptag()
        r = self.corptag.add_corptag(name)
        tag_id = jsonpath(r, f"$..tag[?(@.name=='{name}')]")[0]["id"]
        r = self.corptag.delete_corptag(tag_id=[tag_id])
        assert r["errcode"] == 0
        print("\n删除企业标签的用例通过")

    @pytest.mark.parametrize("name", data["test_delete"])
    def test_delete_api(self, name):
        r = self.corptag.add_api(name)
        tag_id = jsonpath(r, f"$..tag[?(@.name=='{name}')]")[0]["id"]
        r = self.corptag.delete_api(tag_id=[tag_id])
        assert r["errcode"] == 0
        print("\n通过数据驱动删除企业标签通过")

    @classmethod
    def reset(cls):
        r = cls.corptag.get_corptag()
        for name in cls.data["test_delete"]:
            x = jsonpath(r, f"$..tag[?(@.name=='{name}')]")
            if isinstance(x, list) and len(x) > 0:
                cls.corptag.delete_corptag(tag_id=[x[0]["id"]])
