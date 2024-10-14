import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(10)


value=driver.execute_script("return window.pageYOffset;")
print("The scroll pixel initial value =",value)


#Scroll down the page by pixel
driver.execute_script("window.scrollBy(0,900)","")
time.sleep(5)


value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
time.sleep(5)


driver.close()


#Scrolling the Page
#Example 2 ==> Scroll till the element is visible
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)


driver.switch_to.frame("frame-one796456169")
slide_bar=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")


driver.execute_script("arguments[0].scrollIntoView();",slide_bar)
time.sleep(5)


value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
driver.refresh()
time.sleep(5)


#Scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
time.sleep(5)


#Scroll to the Starting Position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
time.sleep(5)


driver.close()

