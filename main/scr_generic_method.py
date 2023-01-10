from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Click_Check():
    def test(self):
        baseURL = "https://www.google.com/"
        cd_service = Service(executable_path='../driver/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=cd_service)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        input_field = driver.find_element(By.XPATH, "//input[@title='Search']")
        time.sleep(4)
        text='lucknow'
        input_field.send_keys(text)
        self.take_screenshot(driver)


    def take_screenshot(self,driver):
            filename=str(round(time.time()*1000))+".png"
            scr_dir="/home/devslane-75/PycharmProjects/selenium_practise/scr/"
            destination_file=scr_dir+filename
            print(destination_file)
            try:
                driver.save_screenshot(destination_file)
                print(f'file saved in dir : {scr_dir}')
            except:
                print("Error")



ff_test = Click_Check()
ff_test.test()