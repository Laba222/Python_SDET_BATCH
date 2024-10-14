from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

driver=webdriver.Chrome()

try:
    # Navigate to Google
    driver.get('https://www.google.com')
    driver.maximize_window()

    # Locate the Google search input box
    search_box = driver.find_element(By.NAME, 'q')

    # Enter the search term
    search_term = 'Python Selenium'
    search_box.send_keys(search_term)

    # Wait for autosuggestions to appear
    wait = WebDriverWait(driver, 10)
    autosuggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="listbox"] li')))

    # Print each autosuggestion
    print("Autosuggestions for:", search_term)
    for suggestion in autosuggestions:
        print(suggestion.text)

finally:
    # Close the browser
    driver.quit()
