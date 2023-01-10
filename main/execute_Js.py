from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class execute_JS():
    def test(self):
        baseURL="https://courses.letskodeit.com/practice"
        cd_service = Service(executable_path="../driver/chromedriver_linux64/chromedriver")
        driver=webdriver.Chrome(service=cd_service)
        #driver.get(baseURL)
        driver.execute_script("window.location='https://courses.letskodeit.com/practice'")
        #element = driver.find_element(By.ID, "bmwradio")
        element= driver.execute_script("return document.getElementById('bmwradio')")
        time.sleep(5)
        element.click()
        driver.quit()

ex_js= execute_JS()
ex_js.test()