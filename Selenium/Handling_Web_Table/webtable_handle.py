import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
#Find the total Number of Rows and Columns:
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print("The number of rows =",rows)


columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
print("The number of column =",columns)


list=[]
#Now I want to go and read all row and column text
for r in range(2,rows+1):
    for c in range(1,columns+1):
        ele_text=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+ "]/td[" +str(c) +"]")
        list.append(ele_text.text)

print(list)




# #I want to read 4th row and 1st column data
# exp_res="Learn JS"
# assert driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[4]/td[1]").text==exp_res
# driver.close()

