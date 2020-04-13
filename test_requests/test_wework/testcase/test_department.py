from test_requests.test_wework.api.department import Department


class TestDepartment:
    proxies = {
        "http": "http://127.0.0.1:8998",
        "https": "https://127.0.0.1:8998"
    }

    @classmethod
    def setup(cls):
        cls.department = Department()

    def test_create_department(self):
        r = self.department.create_department(name="部门003", parentid=1)
        assert r["errcode"] == 0

    def test_delete_department(self):
        r = self.department.delete_department(id=4)
        assert r["errcode"] == 0

    def test_update_department(self):
        r = self.department.update_department(id=8, name="部门004")
        assert r["errcode"] == 0

    def test_check_department(self):
        r = self.department.check_department()
        assert r["errcode"] == 0
        print("\n部门总个数是：{}".format(len(r["department"])))
