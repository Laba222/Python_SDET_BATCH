# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com/")
# time.sleep(5)
# driver.maximize_window()
# expect_title="Google"
# actual_title=driver.title
# print(actual_title)
#
# if actual_title== expect_title:
#     print("test pass")
# else:
#     print("test fail")
# time.sleep(5)
# driver.close()


#Case 2 Firefox
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


option=Options()
option.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"


driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=option)


driver.get("https://google.com")
time.sleep(5)
driver.maximize_window()
expected_title="Google"
actual_title=driver.title
print(actual_title)


if actual_title==expected_title:
   print("Test Pass in Firefox Browser")
else:
   print("Test Fail in Firefox Browser")


time.sleep(5)
driver.close()


#Case 3  Edge
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://google.com")
time.sleep(5)
driver.maximize_window()
expected_title="Google"
actual_title=driver.title
print(actual_title)
time.sleep(5)
if actual_title==expected_title:
   print("Test Pass in Edge Browser")
else:
   print("Test Fail in Edge Browser")
time.sleep(5)
driver.close()

