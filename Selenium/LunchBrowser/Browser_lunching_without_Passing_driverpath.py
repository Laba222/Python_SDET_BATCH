import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(5)
driver.maximize_window()
expect_title="Google"
actual_title=driver.title
print(actual_title)

if actual_title== expect_title:
    print("test pass")
else:
    print("test fail")
time.sleep(5)
driver.close()

# Case -2
# lunch firefox browser

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

option=Options()
option.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"

driver=webdriver.Firefox(options=option)
driver.get("https://www.google.com/")
time.sleep(5)
driver.maximize_window()
expect_title="Google"
actual_title=driver.title
print(actual_title)

if actual_title== expect_title:
    print("test pass")
else:
    print("test fail")

time.sleep(5)
driver.close()

# edge
import time
from selenium import webdriver

driver=webdriver.Edge()
driver.get("https://www.google.com/")
time.sleep(5)
driver.maximize_window()
expect_title="Google"
actual_title=driver.title
print(actual_title)

if actual_title== expect_title:
    print("test pass")
else:
    print("test fail")

time.sleep(5)
driver.close()



print("-----------------------")

