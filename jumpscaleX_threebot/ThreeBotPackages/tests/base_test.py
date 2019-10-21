from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from testconfig import config
import unittest, time
from loguru import logger


class BaseTest(unittest.TestCase):
    LOGGER = logger
    LOGGER.add("apps_{time}.log")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = config["main"]["url"]
        self.browser = config["main"]["browser"]
        self.alerta_page = self.url + "/alerta"
        self.myjobs_page = self.url + "/myjobs"
        self.blog = self.url + "blog"
        self.pastebin = self.url + "pastebin"

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self.set_browser()

        self.driver.set_window_size(1800, 1000)
        self.wait = WebDriverWait(self.driver, 15)

    def set_browser(self):
        if self.browser == "chrome":
            self.driver = webdriver.Chrome()
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.fail("Invalid browser configuration [%s]" % self.browser)

    def get_page(self, page_url):
        try:
            self.driver.get(page_url)
        except Exception as e:
            self.info(" * %s Exception at get_page(%s) " % (str(e), page_url))
        else:
            self.maximize_window()

    def maximize_window(self):
        time.sleep(1)
        screen_dimention = self.driver.get_window_size()
        screen_size = screen_dimention["width"] * screen_dimention["height"]
        if screen_size < 1800 * 1000:
            self.driver.set_window_size(1800, 1000)

    @staticmethod
    def info(message):
        BaseTest.LOGGER.info(message)
