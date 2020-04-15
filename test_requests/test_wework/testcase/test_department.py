from test_requests.test_wework.api.department import Department


class TestDepartment:
    proxies = {
        "http": "http://127.0.0.1:8998",
        "https": "https://127.0.0.1:8998"
    }

    @classmethod
    def setup(cls):
        cls.department = Department()

    # 测试创建部门
    def test_create_department(self):
        r = self.department.create_department(name="部门003", parentid=1)
        assert r["errcode"] == 0

    # 测试创建已存在的部门
    def test_department_existed(self):
        r = self.department.create_department(name="部门003", parentid=1)
        assert r["errcode"] == 60008
        assert "department existed" in r["errmsg"]

    # 测试创建的部门名称超过限制长度
    def test_create_longname(self):
        r = self.department.create_department(name="测试创建一个部门的名称超过32个字符测试创建一个部门的名称超过32个字符", parentid=1)
        assert r["errcode"] == 60001
        assert "department invalid length" in r["errmsg"]

    # 测试创建的部门名称包含不允许的特殊字符
    def test_create_invalid(self):
        r = self.department.create_department(name="测试特殊\:?”<>｜字符", parentid=1)
        assert r["errcode"] == 60009
        assert "department name include invalid char" in r["errmsg"]

    # 测试创建部门的父部门不存在
    def test_create_no_father(self):
        r = self.department.create_department(name="父部门不存在", parentid=0)
        assert r["errcode"] == 60004
        assert "parent department not found" in r["errmsg"]

    # 测试删除部门
    def test_delete_department(self):
        r = self.department.delete_department(id=4)
        assert r["errcode"] == 0

    # 测试删除不存在的部门
    def test_delete_no_exist(self):
        r = self.department.delete_department(id=4)
        assert r["errcode"] == 60123
        assert "invalid party id" in r["errmsg"]

    # 测试删除成员不为空的部门
    def test_delete_contains_user(self):
        r = self.department.delete_department(id=2)
        assert r["errcode"] == 60005
        assert "department contains user" in r["errmsg"]

    # 测试修改部门
    def test_update_department(self):
        r = self.department.update_department(id=8, name="部门004")
        assert r["errcode"] == 0

    # 测试修改不存在的部门
    def test_update_no_exist(self):
        r = self.department.update_department(id=88, name="部门004")
        assert r["errcode"] == 60003
        assert "department not found" in r["errmsg"]

    # 测试查看部门
    def test_check_department(self):
        r = self.department.check_department()
        assert r["errcode"] == 0
        print("\n部门总个数是：{}".format(len(r["department"])))
