# Case One
# lunch chrome Browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj=Service("C:\\driver\\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj)
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
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

option=Options()
option.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# Options(): Initializes an Options object, which will hold various configurations for the Firefox browser.
# binary_location: Specifies the location of the Firefox executable.
# This is necessary if Firefox is not installed in the default location.

service_obj=Service("C:\\driver\\geckodriver.exe")

driver=webdriver.Firefox(service=service_obj,options=option)

# webdriver.Firefox: This initializes the Firefox browser instance using the specified Service and Options.
# service=service_obj: Passes the Service object, which handles the GeckoDriver.
# options=option: Passes the Options object,
# which includes settings like the location of the Firefox executable.

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

# case -3
# Lunch browser in Microsoft Edge

import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
service_obj=Service("C:\\driver\\msedgedriver.exe")

driver=webdriver.Edge(service=service_obj)
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

