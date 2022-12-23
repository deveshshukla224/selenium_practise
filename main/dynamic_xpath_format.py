from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        time.sleep(2)

        # Login -> Lecture "How to click and type on a web element"
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email = driver.find_element(By.ID, "email")
        time.sleep(2)
        email.send_keys("testing100718@gmail.com")
        time.sleep(2)
        password = driver.find_element(By.ID, "password")
        time.sleep(2)
        password.send_keys("secret")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()


        #click on all courses link
        courses_btn = driver.find_element(By.XPATH,"//a[@href='/courses']")
        time.sleep(2)
        courses_btn.click()
        time.sleep(2)

        #dropdown selection

        selection_parent = driver.find_element(By.XPATH, "//select[@name='categories']")
        sel = Select(selection_parent)
        sel.select_by_visible_text("Software Development")
        time.sleep(10)

        # search box
        search_box = driver.find_element(By.XPATH, "//input[@id='search']")
        search_box.send_keys("javascript")
        btn_search_box= driver.find_element(By.XPATH, "//*[@id='search']/div/button")
        time.sleep(2)
        btn_search_box.click()


        # Select Course - dynamic xpath creation
        _course = "//h4[contains(text(),'{0}') and contains(@class,'dynamic-heading')]"
        #{0} - will be replaced by formated value
        _course_format=_course.format("JavaScript for beginners")
        # format is used to replace things
        _course_element=driver.find_element(By.XPATH,_course_format)
        _course_element.click()


ff = DynamicXPathFormat()
ff.test()