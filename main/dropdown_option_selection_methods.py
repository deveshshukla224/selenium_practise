from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
class DrowDown_Option():
    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        element = driver.find_element(By.ID, "carselect")
        selectedElementsList = Select(element)
        time.sleep(10)
        a = selectedElementsList.select_by_index(2)
        time.sleep(10)
        b = selectedElementsList.select_by_value("honda")
        time.sleep(10)
        c = selectedElementsList.select_by_visible_text("Benz")
        time.sleep(10)
        d = selectedElementsList.select_by_index("1")
        time.sleep(10)
        print(a)
        print(b)
        print(c)
        print(d)

dd = DrowDown_Option()


dd.test()