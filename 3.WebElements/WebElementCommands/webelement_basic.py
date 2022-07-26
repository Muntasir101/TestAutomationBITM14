# Commands:
# 1. Click
# 2. Type
# 3. clear
# 4. text
# 5. size
# 6. state of Elements

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class WebElements():

    def basic_commands(self):
        # launch Firefox
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # open url in browser
        driver.get('https://opensource-demo.orangehrmlive.com/')

        # Locate webelements
        username = driver.find_element(By.ID, 'txtUsername')
        password = driver.find_element(By.ID, 'txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.send_keys('Admin')
        password.send_keys('admin123')
        login_btn.click()

        time.sleep(5)

        # close
        driver.close()


obj = WebElements()
obj.basic_commands()


