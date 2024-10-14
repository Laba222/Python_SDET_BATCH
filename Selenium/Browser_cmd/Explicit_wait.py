import time
# ex-1
from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *

# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# wait=WebDriverWait(driver,10,3)
# dynamic_btn=wait.until(EC.presence_of_element_located((By.ID,"dynamic_btn")))
# dynamic_btn.click()
# time.sleep(5)
# driver.close()

# ex-2
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# try:
#    wait=WebDriverWait(driver,10,3)
#    dynamic_btn=wait.until(EC.element_to_be_clickable((By.ID,"dynamic_btn")))
# except:
#    dynamic_btn.click()
# finally:
#
#    driver.close()

# ex-3

driver=webdriver.Chrome()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
try:
   wait=WebDriverWait(driver,10,3,(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,Exception))
   dynamic_btn=wait.until(EC.element_to_be_clickable((By.ID,"dynamic_btn")))
except:
   dynamic_btn.click()
finally:

   driver.close()