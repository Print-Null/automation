import yaml


class TestYAML:
    def test_yaml(self):
        print(yaml.safe_load(open(r"D:\MyProjects\test_appium\page\steps.yaml")))

