from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class scroll_functons():
    def scroll(self):
        baseURL="https://courses.letskodeit.com/practice"
        cd_service = Service(executable_path="../driver/chromedriver_linux64/chromedriver")
        driver=webdriver.Chrome(service=cd_service)
        driver.maximize_window()
        driver.get(baseURL)
        time.sleep(3)
        #scroll down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)
        #scroll up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)

        #scroll_element_into_view
        element=driver.find_element(By.ID, "mousehover")
        #driver.execute_script("arguments[0].scrollIntoView(true);",element)
        #driver.execute_script("window.scrollBy(0,-100);")
        time.sleep(3)

        #native_way to scroll_into view
        driver.execute_script("window.scrollBy(0,-1000);")
        element.location_once_scrolled_into_view
        time.sleep(5)

        driver.quit()
hw=scroll_functons()
hw.scroll()