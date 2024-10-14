from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()

# driver.get("https://www.facebook.com/r.php?locale=en_GB&display=page")
# driver.maximize_window()
# time.sleep(4)
# element=driver.find_element(By.XPATH,"//div[@id='reg_form_box']/child::div[11]/button")
# print(element.text)
# time.sleep(3)
# element.click()
# print("Element is successfully clicked")
# time.sleep(4)
# driver.close()


# parent axes

driver.get("https://www.google.com/webhp?authuser=1")
driver.maximize_window()
time.sleep(3)
elmnt=driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']/parent::*/parent::*/parent::*/div[1]")
time.sleep(3)
elmnt.click()
time.sleep(4)
elmnt.send_keys("QAcircleAcademy")
print("Test pass")
time.sleep(4)
driver.close()

