from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

class calenderSelection():
    def test(self):
        baseURL = "https://www.makemytrip.com/"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.get(baseURL)
        driver.implicitly_wait(10)
        element_selection=driver.find_element(By.XPATH, "//div[contains(@class,'fsw_inputBox dates inactiveWidget')]")
        time.sleep(5)
        element_selection.click()
        date_selection=driver.find_element(By.XPATH,"//div[@class='DayPicker-Months']//div[1]//div[@class='DayPicker-Body']//div[5]//div[6]//div[1]")
        time.sleep(10)
        date_selection.click()
        search_btn= driver.find_element(By.XPATH,"//a[contains(text(),'Search')]")
        time.sleep(4)
        search_btn.click()





cs_test = calenderSelection()
cs_test.test()