import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()


#Find the total Number of Rows and Columns:
rows=len(driver.find_elements(By.XPATH,"//table[@class='dataTable']//tr"))
print("The number of rows =",rows)


columns=len(driver.find_elements(By.XPATH,"//table[@class='dataTable']//tr/th"))
print("The number of column =",columns)


#I want to read all the row and column
# for r in range(2,rows+1):
#     for c in range(1,columns+1):
#         ele_text=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr["+str(r)+ "]/td[" +str(c) +"]").text
#         print(ele_text ," ", end='  ')
#     print()


#I want to read
Raymond_Xpath="//table[@class='dataTable']/tbody/tr[12]"
print(driver.find_element(By.XPATH,Raymond_Xpath).text)
list=[]
for c in range(4,columns):
   data=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[12]/td["+str(c)+"]").text
   list.append(data)


print("The Raymond Current Price is =",list[0])
print("The Raymond % Change is =",list[1])
driver.close()


