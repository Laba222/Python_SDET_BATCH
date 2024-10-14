from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
# driver.get("https://www.nykaa.com/")
# driver.maximize_window()
# time.sleep(4)
# driver.find_element(By.XPATH,"//button[contains(@kind,'primary')]").click()
# driver.close()


driver.get("https://www.firstcry.com/")
driver.maximize_window()
# x=driver.find_element(By.XPATH,"//span[text()='Track Order']")
# print(x.text)
# if "Track Order"==x.text:
#     x.click()
# time.sleep(5)

z = driver.find_element(By.XPATH, "//span[text()='FirstCry Parenting']")
print(z.text)
# if "FirstCry Parenting" == z.text:
#     z.click()
#     assert "Baby Products Online India: Newborn Baby Products & Kids Online Shopping at FirstCry.com"==driver.title
#     print("my test case is pass")


y=driver.find_element(By.XPATH, "//span[contains(text(),' Register')]").text
print(y)

driver.close()
