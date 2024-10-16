# # Example 1
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://jqueryui.com/tooltip/")
# driver.maximize_window()
# time.sleep(5)
#
# #Switching frame
# driver.switch_to.frame(0)
#
#
# age_text_field_ele=driver.find_element(By.ID,"age")
# #Print the text of an element. We will get blank line because this element is not having any text
# print(age_text_field_ele.text)
#
# expected_tool_tip="We ask for your age only for statistical purposes."
# actual_tool_tip=age_text_field_ele.get_attribute("title")
# print(actual_tool_tip)
#
# assert expected_tool_tip.__eq__(actual_tool_tip)
#
# time.sleep(5)
# driver.close()



# file:///C:/Users/Kusha/Downloads/SeleniumPythonHybridFramework/htmlprac/tooltip.html

#Example 2
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("///C:/Users/Kusha/Downloads/SeleniumPythonHybridFramework/htmlprac/tooltip.html")
driver.maximize_window()
time.sleep(5)

#locate an element
trigger_element=driver.find_element(By.ID,"trigger-element")
action=ActionChains(driver)
action.move_to_element(trigger_element).perform()

#Wait for the tooltip element until visible
wait=WebDriverWait(driver,10)
tool_tip=wait.until(EC.visibility_of_element_located((By.ID,"tooltip-element")))

#Capture the text of tooltip
print(tool_tip.text)

driver.quit()



