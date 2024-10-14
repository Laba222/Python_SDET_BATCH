# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# driver.find_element(By.ID,"test-alert").click()
# time.sleep(5)
# alert_window=driver.switch_to.alert
# time.sleep(5)
# print(alert_window.text)
# alert_window.accept()
# time.sleep(5)
# driver.close()
#
# print("--------------------------------------------------f")
# # ex-2
#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# time.sleep(5)
# driver.close()
#


# prompt alert

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(5)

window_ele=driver.switch_to.alert
window_ele.send_keys("QACircle Software Training Academy")
window_ele.accept()

exp_result="You entered: QACircle Software Training Academy"

assert exp_result==driver.find_element(By.ID,"result").text,"Both element texts are different"

# time.sleep(5)
# driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
# time.sleep(5)
#
# window_ele=driver.switch_to.alert
# window_ele.send_keys("QACircle Software Training Academy")
# window_ele.dismiss()
#
# exp_re="You entered: null"
#
# assert exp_re==driver.find_element(By.ID,"result").text
driver.close()
