from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service
#import statement for adding explicit wait types
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitDemo1():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.execute_script("window.location = 'https://courses.letskodeit.com/';")
        # driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
        #3 arguments in WebDriverWait - driver , timeout , poll_frequency , ignored_expection
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                                                ignored_exceptions=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sign In']")))
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo1()
ff.test()
