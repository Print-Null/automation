from test_selenium.page.manage_tool import ManageTool


class TestImage:
    mt = ManageTool(reuse=True)

    def test_upload_image(self):
        self.mt.goto_material_library().upload_image(r"C:\Users\Administrator\Desktop\微信图片_20200212171843.jpg")

    def test_delete_image(self):
        self.mt.goto_material_library().delete_image()
