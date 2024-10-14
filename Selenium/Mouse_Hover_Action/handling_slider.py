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


driver.switch_to.frame(0)
min_slider=driver.find_element(By.XPATH,"//div[@id='slider']/span")
print(min_slider.location)


act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,200,200).perform()
time.sleep(5)
print(min_slider.location)
driver.close()
