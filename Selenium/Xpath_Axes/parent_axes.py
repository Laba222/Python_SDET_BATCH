import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)
# Wait for the search box to be present
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q")))


# Enter a search term in the search box
search_box.send_keys("Selenium Python tutorial")
time.sleep(5)
# Press Enter or click on the search button
search_box.send_keys(Keys.RETURN)  # This mimics pressing the Enter key
time.sleep(5)


# Close the browser (optional)
driver.quit()
