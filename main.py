from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

"""
Access website
Select input field, add text, submit

"""

chromedriver_path = 'chromedriver.exe'

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

url = "https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes"


def apply_and_submit(frame, data, submit, enter):
    fr = driver.find_element(By.ID, frame)
    driver.switch_to.frame(fr)
    inp = driver.find_element(By.ID, data)
    ActionChains(driver) \
        .scroll_to_element(inp) \
        .perform()
    inp.click()
    inp.send_keys("justinolson624@gmail.com")
    sub = driver.find_element(By.ID, submit)
    sub.click()
    time.sleep(10)
    ent = driver.find_element(By.CLASS_NAME, enter)
    ent.click()
    time.sleep(10)


try:
    driver.get(url)
    print("Website accessed!")
    time.sleep(5)
    # frame = driver.find_element(By.ID, "ngxFrame270554")
    # driver.switch_to.frame(frame)
    # print("Frame found and selected.")
    # time.sleep(5)
    # email_input = driver.find_element(By.ID, "xReturningUserEmail")
    # ActionChains(driver) \
    #     .scroll_to_element(email_input) \
    #     .perform()
    # print("Email input found.")
    # email_input.click()
    # print("Email input clicked.")
    # email_input.send_keys("TEST")
    # print("Text input into field.")
    # time.sleep(5)
    # submit = driver.find_element(By.ID, "xCheckUser")
    # submit.click()
    apply_and_submit("ngxFrame270554", "xReturningUserEmail", "xCheckUser", "xButton")
    print("HGTV Submitted.")
    time.sleep(10)
    food_link = driver.find_element(By.CLASS_NAME, "editorial-link-no-style")
    food_link.click()
    # Should direct to https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-smart-home-sweepstakes?xp=sistersite
    time.sleep(10)
    apply_and_submit("ngxFrame270556", "xReturningUserEmail", "xCheckUser", "xButton")
    print("Food Network Submitted")
    time.sleep(10)

finally:
    # Always close the driver
    driver.quit()
    print("Browser closed.")
