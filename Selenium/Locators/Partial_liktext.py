import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/downloads/")
time.sleep(5)
#driver.find_element(By.PARTIAL_LINK_TEXT,"Proj").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"jects").click()


time.sleep(5)
driver.close()
