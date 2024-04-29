from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = 'chromedriver.exe'

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

url = "https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes"

try:
    driver.get(url)
    print("Website accessed!")
    time.sleep(5)
    frame = driver.find_element(By.ID, "ngxFrame270554")
    driver.switch_to.frame(frame)
    print("Frame found and selected.")
    time.sleep(5)
    email_input = driver.find_element(By.ID, "xReturningUserEmail")
    print("Email input found.")
    email_input.click()
    print("Email input clicked.")
    email_input.send_keys("TEST")
    print("Text input into field.")
    time.sleep(5)

finally:
    # Always close the driver
    driver.quit()
    print("Browser closed.")
