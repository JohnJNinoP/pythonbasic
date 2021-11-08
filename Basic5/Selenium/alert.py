from logging import setLogRecordFactory
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class CompareProducts(unittest.TestCase):
    def sepUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_compare_products_remove_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_id("q")
        search_field.clear()
        search_field.send_keys("tee")
        search_field.submit()

        driver.find_element_by_class_name("link-compare").click()

        driver.find_element_by_link_text("Clear All").click()

        alert = driver.switch_to_alert()
        alert_text = alert.text

        
    

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1')) , 

        