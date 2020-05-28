import logging
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 定义打印的log级别为INFO级别
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    # 定义异常黑名单列表
    _black_list = [
        (By.ID, "tv_agree"),
        (By.XPATH, "//*[@text='确定']"),
        (By.ID, "image_cancel"),
        (By.ID, "tv_left"),
        (By.ID, "ib_close")
    ]
    # 定义最大的异常处理次数
    _error_max = 3
    # 定义异常处理次数的计数器
    _error_count = 0
    _params = {}

    # 初始化driver，限定driver为WebDriver类型，默认值为None
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 二次封装默认的find_element方法
    def find(self, by, locator: str = None):
        logging.info(by)
        logging.info(locator)
        try:
            # if else的特殊写法，如果find方法传一个元组参数则拆元组并使用if前面的语句，如果是两个参数则使用else后边的语句
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                             locator)
            # 如果找到了原本要定位的元素则异常处理计数器归0并返回该元素，若没找到则进入异常处理流程
            self._error_count = 0
            return element
        except Exception as e:
            if self._error_count >= self._error_max:
                raise e
            # 每次进入异常处理，则异常处理计数器+1，直到大于定义的最大异常处理次数，则退出异常处理逻辑，直接抛出异常
            self._error_count += 1
            print("第%s次查找异常" % self._error_count)
            # 尝试在异常黑名单里查找导致异常的元素
            for element in self._black_list:
                logging.info(element)
                # find_elements方法返回的是一个列表
                elements = self._driver.find_elements(*element)
                # 如果列表的len大于0则表示导致进入异常处理流程的元素在黑名单列表里
                if len(elements) > 0:
                    # 在黑名单列表中则点击掉它并返回到find方法继续定位原本要定位的元素
                    elements[0].click()
                    return self.find(by, locator)
                # else:
                #     self._error_count += 1
                #     if self._error_count > self._error_max:
                #         raise e
            # 如果在黑名单列表中没有找到导致异常的元素也抛出异常
            logging.warning("black list no one found")
            raise e

    def data_driven(self, path):
        steps: list[dict] = yaml.safe_load(open(path))
        element: WebElement = None
        for step in steps:
            logging.info(step)
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
                elif action == "text":
                    element.text
                elif action == "attribute":
                    element.get_attribute(step["attribute"])
                elif action == "send":
                    content: str = step["value"]
                    for key in self._params.keys():
                        content = content.replace("{%s}" % key, self._params[key])
                    element.send_keys(content)
