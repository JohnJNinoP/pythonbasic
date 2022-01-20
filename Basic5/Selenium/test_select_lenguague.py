from types import DynamicClassAttribute
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select

class RegisterNewUer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        #driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.implicitly_wait(10)
    def test_select_lenguage(self):
        exp_options = ['English','French','German']
        act_option = []
        select_langueage = Select(self.driver.find_element_by_id('select-language'))
        

        self.assertEqual(3,len(select_langueage.options))

        for option in select_langueage.options:
            act_option.append(option.text)

        self.assertListEqual(exp_options,act_option)

        self.assertEqual('English',select_langueage.first_selected_option.text)

        select_langueage.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)

        self.driver.implicitly_wait(5)

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))