# CSS selector

# ex-1

from selenium import webdriver
from selenium.webdriver.common.by import By
import  time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("QAcircle")
# time.sleep(5)
# driver.close()


# ex-2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("QAcircle")
# time.sleep(5)
# driver.close()

# ex-3

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"div >input#username").send_keys("hello MR'S")
# time.sleep(5)
# driver.close()



# ex-4

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input.input_error.form_input").send_keys("QAcircle")
# time.sleep(5)
# driver.close()


# Find element By using single attribute

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("Hello marry")
# time.sleep(5)
# driver.close()



# Find element By using two attribute
# input[name='user-name'][data-test='username']

from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='user-name'][data-test='username']").send_keys("Hello marry")
time.sleep(5)
driver.close()
print("----------------------------------------------------------------------------------------")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import  time
#
# driver=webdriver.Chrome()
# driver.get("D:\\Python_SDET\\Selenium\\Locators\\nthchild.html")
# driver.maximize_window()
# x=driver.find_element(By.CSS_SELECTOR,"#recordists li:nth-of-type(3)+li")
# y=driver.find_element(By.CSS_SELECTOR,"#recordists li:nth-of-type(1)+li")
# z=driver.find_element(By.CSS_SELECTOR,"#recordists *:nth-child(4)")
#
# print(x.text) # Banana
# print(y.text) # Orange
# print(z.text) # Banana
#
# time.sleep(5)
# driver.close()


print("---------------------------------------------------------------------------------")

# ex-5
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in/")
# driver.maximize_window()
# x=driver.find_element(By.CSS_SELECTOR,".mainMenu li:nth-child(2)")
# y=driver.find_element(By.CSS_SELECTOR,".mainMenu li:nth-child(3)")
# z=driver.find_element(By.CSS_SELECTOR,".mainMenu li:nth-child(5)")
#
# print(x.text) # Banana
# print(y.text) # Orange
# print(z.text) # Banana
#
# time.sleep(5)
# driver.close()


print("--------------------------------------------")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://signup.pcloudyunified.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"div[class='iti__selected-flag'][aria-controls='iti-0__country-listbox']").click()
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:last-child").text)
time.sleep(5)
driver.close()

