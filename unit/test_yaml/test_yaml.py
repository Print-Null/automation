import yaml


class TestYAML:
    def test_yaml(self):
        print(yaml.safe_load(open("test_yaml.yaml", encoding="UTF-8")))
        print(yaml.safe_load(open(r"D:\MyProjects\test_appium\page\search.yaml", encoding="UTF-8")))
