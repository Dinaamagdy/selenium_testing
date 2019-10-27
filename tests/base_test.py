from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from testconfig import config
import unittest, time
from loguru import logger
from Elements import elements
from selenium.webdriver.common.by import By


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
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome(options)

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

    def find_element(self, element):
        method = elements[element][0]
        value = elements[element][1]
        element_value = self.driver.find_element(getattr(By, method), value)
        return element_value

    def get_table_head_elements(self, element):
        table = self.find_element(element)
        thead = table.find_elements_by_tag_name("thead")
        thead_row = thead[0].find_elements_by_tag_name("tr")
        return thead_row[0].find_elements_by_tag_name("th")

    def get_table_rows(self, element=None):

        element = self.find_element(element)
        tbody = element.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        return rows

    def get_table_row(self, table, i):
        table_row = self.get_table_rows(table["data"])[i]
        row_cells = table_row.find_elements_by_tag_name("td")
        self.assertTrue(row_cells)
        return [x.text for x in row_cells]

    @staticmethod
    def info(message):
        BaseTest.LOGGER.info(message)
