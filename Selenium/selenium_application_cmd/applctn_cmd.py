from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://aha.video/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()