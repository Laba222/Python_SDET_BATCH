import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


#Example 1 Chrome Browser


#driver = webdriver.Chrome()
driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")