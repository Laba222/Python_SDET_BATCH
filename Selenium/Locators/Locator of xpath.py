#
# # -----------------------------------Absolute Xpath------------------------------
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
# time.sleep(5)
# driver.close()
#
#
# #--------------------------------Relative Xpath----------------------------------------
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("hello tester")
# time.sleep(5)
#


# xpath for image
from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

driver=webdriver.Chrome()
driver.get("https://mamaearth.in/product-category/rice-range")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//img[@src='https://images.mamaearth.in/wysiwyg/mamaearth-logo.png?format=auto&fit=scale']").click()
time.sleep(4)
driver.close()