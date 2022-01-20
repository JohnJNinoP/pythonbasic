from typing import SupportsAbs
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions  import NoSuchElementException
from selenium.webdriver.common.by import By

class UniteTestHello(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = cls.driver
        #driver.implicitly_wait(10)
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_filed(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")


    #Validar que exista boton
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")
    
    #Validar una clase lista
    def test_count_if_promo_banner_image(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banner = banner_list.find_elements_by_tag_name("img")
        len_banner = len(banner)
        self.assertEqual(3,len_banner)

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('')
        

    # def test_hellow(self):
    #     driver = self.driver
    #     driver.get('https://www.platzi.com')

    # def test_wikipedia(self):
    #     self.driver.get('https://wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))
