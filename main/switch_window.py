from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class switch_window():
    def switch_w(self):
        baseURL="https://courses.letskodeit.com/practice"
        cd_service = Service(executable_path="../driver/chromedriver_linux64/chromedriver")
        driver=webdriver.Chrome(service=cd_service)
        driver.maximize_window()
        driver.get(baseURL)
        time.sleep(3)
        driver.implicitly_wait(5)
        #diffrent windows are identified by handles in selenium
        #driver.current_window_handle - this will return the handle id of first loaded page
        parentHandle = driver.current_window_handle
        print(f'Parent Handle is -{parentHandle}')
        #click on open window to open a diffrent window
        driver.find_element(By.ID,"openwindow").click()
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        #driver.window_handles - will let us know about diffrent handles availble in session
        handles = driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                print(handle)
                driver.switch_to.window(handle)
                driver.maximize_window()
                print(f'switched to window -{handle}')
                login_btn=wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@href="/login"]')))
                #driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
                print(login_btn)
                #print("Element is visible? " + str(search_box.is_displayed()))
                login_btn.click()
                time.sleep(3)
                driver.close()
                break
        time.sleep(2)
        driver.switch_to.window(parentHandle)
        a=driver.current_window_handle
        print(f'switched to {a}')
        text_box=driver.find_element(By.ID,"name")
        time.sleep(3)
        text_box.send_keys("test done")
        driver.quit()


switch_window=switch_window()
switch_window.switch_w()