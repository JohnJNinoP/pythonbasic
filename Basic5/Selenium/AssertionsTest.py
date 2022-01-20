from typing import SupportsAbs
import unittest
from unittest.result import failfast
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions  import NoSuchElementException
from selenium.webdriver.common.by import By

class Assertions_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    def test_search_text_field_by_name(self):
        #search_field = self.driver.find_element_by_name("q")
        self.assertTrue(self.is_element_present(By.NAME , 'q'))

    def test_search_option_lenguage(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how,value= what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))
