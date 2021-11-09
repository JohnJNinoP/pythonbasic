import unittest
from selenium import webdriver
from time import sleep
from pyunitreport import HTMLTestRunner

class AddRemoveElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Add/Remove Elements").click()
    
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input("How many elements will you add"))
        sleep(5)
        elements_remove = int(input("How many elements will you remove"))
        sleep(5)
        total_elements = elements_added - elements_remove
        sleep(2)
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
        for i in range(elements_added ):
            add_button.click()
        
        for i in range(elements_remove):
            try:
                delete_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
                delete_button.click()
            except:
                print("you're trying to delete more elements the existent")

        if total_elements > 0:
            print(f"There are {total_elements}")
        else: 
            print('There are 0 elements')
        sleep(2)

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))
