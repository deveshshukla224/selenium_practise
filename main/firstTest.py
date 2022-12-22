from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Service

class RunChromeTest():
    def test(self):
        ff_service = Service(executable_path='../driver/geckodriver-v0.32.0-linux64/geckodriver')
        driver = webdriver.Firefox(service=ff_service)
        baseURL = "https://letskodeit.teachable.com/"
        title = driver.title
        print("The Title of the web page is :  " + title)
        current_url = driver.current_url
        print("Current URL is " + current_url)
        driver.refresh()
        print("Refreshed Once")
        driver.get(current_url)
        print("Refreshed Second Time")
        driver.get("https://sso.teachable.com/secure/42299/identity/login/password")
        print("Going Backword")
        driver.back()
        print("Backed Sucessfully")
        driver.forward()
        print("Forward successfull")
        driver.close()
ff_test = RunChromeTest()
ff_test.test()