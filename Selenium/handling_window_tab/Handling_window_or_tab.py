import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/auth/login")

driver.maximize_window()
current_window_id=driver.current_window_handle
print(current_window_id)
time.sleep(4)
driver.find_element(By.XPATH,"//a[@href='http://www.orangehrm.com']").click()
# //a[@href='http://www.orangehrm.com']

# find the number of browser  tab
windows=driver.window_handles
print(len(windows))
for i in windows:
    print(i)
print("------------------------------")
print("Parent window ID =",windows[0])
print("Child Window Id =",windows[1])

# Getting title of the tab
print(driver.title)

driver.switch_to.window(windows[1])
print(driver.title)      # Human Resources Management Software | OrangeHRM (Child tab title )
driver.close()

driver.switch_to.window(windows[0])
print(driver.title)      # OrangeHRM (parent window title)
driver.close()

#Use for loop for closing tabs
for window in windows:
   driver.switch_to.window(window)
   if driver.title=="Human Resources Management Software | OrangeHRM" or "OrangeHRM":
       time.sleep(5)
       driver.close()
#time.sleep(5)


# Example -2
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
parent_window=driver.current_window_handle
print(parent_window)
print(driver.title)

driver.find_element(By.LINK_TEXT,"Open a popup window").click()
time.sleep(4)

all_windows=driver.window_handles
print(all_windows)
print(len(all_windows))

# driver.switch_to.window(all_windows[1])
# print(driver.title)

for w in all_windows:
    driver.switch_to.window(w)
    if driver.title.__eq__("New Window"):
        time.sleep(4)
        para_txt=driver.find_element(By.XPATH,"//h3[text()='New Window']").text
        print(para_txt)
        time.sleep(4)
        driver.close()
        break

driver.switch_to.window(parent_window)
driver.close()



# example -3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='New Window']").click()
time.sleep(5)


window_ids=driver.window_handles
for window in window_ids:
   print(window)


print("Parent Window Id", window_ids[0])
print("child Window Id", window_ids[1])


print(driver.title)
driver.switch_to.window(window_ids[1])
print(driver.title)


for window in window_ids:
   driver.switch_to.window(window)
   if driver.title=="QACircle Software Training Academy":
       driver.close()


driver.switch_to.window(window_ids[0])
time.sleep(5)
driver.close()
