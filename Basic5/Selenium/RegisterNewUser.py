from types import DynamicClassAttribute
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class RegisterNewUer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        #driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.implicitly_wait(30)

    def test_new_use(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account',driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        new_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and new_letter_subscription.is_enabled()
        and submit_button.is_enabled())
        
        first_name.send_keys('Test1')
        middle_name.send_keys('Middle1')
        last_name.send_keys('Tes1t')
        email.send_keys('Test1@mail2.com')
        password.send_keys('Test1234516')
        confirm_password.send_keys('Test1234516')
        submit_button.click()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))