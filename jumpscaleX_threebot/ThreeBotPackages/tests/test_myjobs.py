from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from testconfig import config
import unittest, time
from base_test import BaseTest


class Myjobs(BaseTest):
    def Setup(self):
        self.get_page(self.url)

    def test01_testsearch(self):
        """
        * test
        """
        pass
