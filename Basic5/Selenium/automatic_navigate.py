from types import DynamicClassAttribute
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        #driver.maximize_window()
        driver.get('https://google.com/')
        driver.implicitly_wait(10)
    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("platzy")
        search_field.submit()
        
        driver.back()
        driver.forward()
        driver.refresh()

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))
