from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    # Let's wait for 10 seconds or perform some tasks
    time.sleep(10)  # It's better to use explicit waits conditionally

finally:
    # Always close the driver
    driver.quit()
    print("Browser closed.")
