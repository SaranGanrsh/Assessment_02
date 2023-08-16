import time

import app
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]").click()
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset").click()
time.sleep(30)
driver.quit()
