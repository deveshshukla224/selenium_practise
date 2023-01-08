from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class autoComplete():
    def method(self):
        baseURL = "https://www.google.com/"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        text="del"
        text_to_match="delhi temperature"
        driver.get(baseURL)
        driver.maximize_window()
        input_field = driver.find_element(By.XPATH, "//input[@title='Search']")
        time.sleep(4)
        input_field.send_keys(text)
        wait = WebDriverWait(driver, timeout=30, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']")))
        liItem=element.find_elements(By.TAG_NAME,'li')
        for item in liItem:
            if(text_to_match in item.text):
                item.click()
                break
        driver.quit()



autoC= autoComplete()
autoC.method()