from selenium import webdriver
from selenium.webdriver.common.by import By
from handy_wrappers import HandyWrappers
from selenium.webdriver.firefox.service import Service
import time


class ElementPresentCheck():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()