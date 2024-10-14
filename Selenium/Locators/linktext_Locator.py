# EX ---1
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# time.sleep(5)
# driver.get("D:\\Python_SDET\\Selenium\\Locators\\linktext.html")
# driver.find_element(By.LINK_TEXT,"Continue").click()
# time.sleep(5)
# driver.close()


# EX ---2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("https://www.selenium.dev/downloads/")
driver.find_element(By.LINK_TEXT,"Projects").click()

txt=driver.find_element(By.XPATH,"//h2[normalize-space()='Selenium WebDriver']").text
print(txt)


time.sleep(5)
driver.close()
