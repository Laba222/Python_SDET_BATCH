import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

time.sleep(3)

dropdown=driver.find_element(By.ID,"drop1")
select=Select(dropdown)
# select.select_by_visible_text("doc 3")
# select.select_by_index(3)
# select.deselect_by_value("project-4")
# print(select.first_selected_option.text)
dropdown=select.options
for o in dropdown:
    print(o.text)

driver.quit()

# output
# Older Newsletters
# doc 1
# doc 2
# doc 3
# doc 4


# how to handle multi select drop down

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()

# mul_sel_drop_down=Select(driver.find_element(By.ID,'colors'))
# print(mul_sel_drop_down.is_multiple) # true
# mul_sel_drop_down.select_by_value("green")
# time.sleep(5)
# mul_sel_drop_down.select_by_visible_text("Yellow")
# time.sleep(5)
# mul_sel_drop_down.select_by_index(1)
# time.sleep(5)
# mul_sel_drop_down.deselect_by_visible_text("Green")
# time.sleep(5)
# mul_sel_drop_down.deselect_by_value("yellow")
# time.sleep(5)
# mul_sel_drop_down.deselect_by_index(1)

# driver.close()

# print(mul_sel_drop_down.first_selected_option.text)
# all_selected=mul_sel_drop_down.all_selected_options
# for x in all_selected:
#     print(x.text)
# time.sleep(5)
# mul_sel_drop_down.deselect_all()
# time.sleep(5)
# driver.close()

# Handle drop down without using select class

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# list=driver.find_elements(By.ID,"colors")
#
# for x in list:
#    print(x.text)
#    x.click()
#    time.sleep(5)
#
# time.sleep(5)
# driver.close()



import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
drop_down=Select(driver.find_element(By.ID,"country"))
all_options=drop_down.options
#get the text of all the elements
for option in all_options:
    print(option.text)
time.sleep(5)

