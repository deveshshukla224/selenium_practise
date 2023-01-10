from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class Click_Check():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/"
        cd_service = Service(executable_path='../driver/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=cd_service)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        print(driver.current_url)
        login_link = driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        login_link.click()
        emailField = driver.find_element(By.XPATH, "//input[@id='email']")
        emailField.send_keys("test")
        time.sleep(5)
        passwordField = driver.find_element(By.XPATH, "//input[@id='password']")
        time.sleep(5)
        passwordField.send_keys("test")
        time.sleep(5)
ff_test = Click_Check()
ff_test.test()