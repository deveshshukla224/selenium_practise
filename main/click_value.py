from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
class Click_Check():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        print(driver.current_url)
        login_link = driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        login_link.click()
        time.sleep(5)
        print(driver.current_url)
        emailField = driver.find_element(By.XPATH, "//input[@id='email']")
        emailField.send_keys("test")
        time.sleep(5)
        passwordField = driver.find_element(By.XPATH, "//input[@id='password']")
        time.sleep(5)
        passwordField.send_keys("test")
        time.sleep(5)
ff_test = Click_Check()
ff_test.test()