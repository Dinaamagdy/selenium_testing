from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from testconfig import config
import unittest, time
from .base_test import BaseTest


class Myjobs(BaseTest):
    def Setup(self):
        self.get_page(self.myjobs_page)
        self.assertIn("Myjobs Visualizer", self.driver.title)
        self.find_element("Jobs_bage").Click()
        self.assertIn("tasks", self.driver.current_url)
        self.rows_count = self.driver.execute_script("return document.getElementsByTagName('tr').length") - 2
        self.summary_table = self.find_element("summary_table")
        self.jobs_table = self.find_element("jobs_table")

    def test01_check_summary_table_head_elements(self):
        """
        * Check  summary table head elements *
        - Get all head values and check it is as expected .
        """
        expected_head_elements = [
            "Total Tasks",
            "Success Tasks",
            "Failure Tasks",
            "New Tasks",
            "Running Tasks",
            "Halted Tasks",
        ]
        head_element = self.get_table_head_elements("summary_table")
        self.assertEqual(set(expected_head_elements), set(head_element))

    def test001_ALL_filter_in_jobs_page(self):
        """
        * test ALL filter *
        - Get jobs page. 
        - Click All filter , Check that it return all jobs.
        - Check that it has same value as all jobs value in summary table.
        """

        self.info("Click All filter , Check that it return all jobs.")
        All_element = self.find_element("ALL_filter")
        All_element.Click()
        rows_count_after_all = self.driver.execute_script("return document.getElementsByTagName('tr').length") - 2
        self.assertEqual(rows_count_after_all, self.rows_count)
        summary

    def test002_Success_filter_in_jobs_page(self):
        """
        * test filters [Success, Failure, New, Running, Halted ] in jobs page.*  
        - Get jobs page. 
        - Click Success filter , Check that it return sucsess jobs only .
        
        """
        rows_count = driver.execute_script("return document.getElementsByTagName('tr').length") - 2
        All_element = self.find_element("Success_filter")
        All_element.Click()
        rows_count_after_all = driver.execute_script("return document.getElementsByTagName('tr').length") - 2
        self.assertEqual(rows_count_after_all, rows_count)
