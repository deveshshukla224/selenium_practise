from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

class Click_Check():
    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        bmw_radio=driver.find_element(By.XPATH, '//input[@id="bmwradio"]')
        bmw_radio.click()
        time.sleep(5)
        benz_radio=driver.find_element(By.XPATH, '//input[@id="benzradio"]')
        benz_radio.click()
        time.sleep(5)
        print("Radio Button is opted ? " + str(benz_radio.is_selected()))
        bmw_check=driver.find_element(By.ID, "bmwcheck")
        bmw_check.click()
        print("Checbox is selected ? " + str(bmw_check.is_selected()))

cc=Click_Check()
cc.test()
