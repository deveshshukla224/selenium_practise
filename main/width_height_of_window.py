from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class hw():
    def he_wi(self):
        baseURL="https://courses.letskodeit.com/practice"
        cd_service = Service(executable_path="../driver/chromedriver_linux64/chromedriver")
        driver=webdriver.Chrome(service=cd_service)
        driver.get(baseURL)
        driver.maximize_window()
        width = str(driver.execute_script("return window.innerWidth;"))
        height= str(driver.execute_script("return window.innerHeight;"))
        print(f'Width of window is {width} and Height is {height}')
        driver.quit()
hw=hw()
hw.he_wi()