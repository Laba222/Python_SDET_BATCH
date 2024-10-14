from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(4)
# e=driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']/center/input[1]")
#
# print(e.is_displayed())
#
# print(driver.find_element(By.XPATH,"//textarea[@name='q']").is_enabled())
# time.sleep(5)
# driver.close()

# xpath for radio button ---> //input[@type='radio']

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
time.sleep(2)
e=driver.find_elements(By.XPATH,"//input[@type='radio']")
for i in e:
    print(i.is_displayed())
time.sleep(5)

print("-------------------------------------check select box-------------------------------------------------------")
for i in e:
    print(i.is_selected())
print("-------------------------------check multiple check box is selected or not ----------------------------")
for i in e:
    i.click()
    print(i.is_selected())
time.sleep(5)
print("------------------------------- enabled or not check----------------------------")
for i in e:
    print(i.is_enabled())
time.sleep(5)
driver.close()

