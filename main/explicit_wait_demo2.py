from selenium import webdriver
import time
from explicit_wait_type import ExplicitWaitType
from selenium.webdriver.firefox.service import Service

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="//a[text()='Sign In']", locatorType="xpath")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()