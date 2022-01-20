import unittest
from selenium import webdriver
from time import sleep
from pyunitreport import HTMLTestRunner

class AddRemoveElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'F:\John\Proyectos\Python\pt\pythonbasic\Drivers and promgrams\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Disappearing Elements").click()
    
    def test_name_element(self):
        driver = self.driver

        options = []
        menu = 5

        tries = 1

        while(len(options)<5):
            options.clear()
            driver.refresh()
            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'option number {i + 1 } is NOT FOUND')
                    tries += 1
            
            sleep(1)
            
        
        print(f'Finished in {tries} tries')

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity= 2 , testRunner=HTMLTestRunner(output='Reportes',report_name='Reposte1'))
