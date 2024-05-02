from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
    print("Frame switched.")
    inp = driver.find_element(By.ID, data)
    print("Input field focused.")
    inp.click()
    inp.send_keys("justinolson624@gmail.com")
    print("Email input.")
    time.sleep(2)
    sub = driver.find_element(By.ID, submit)
    sub.click()
    print("Submit clicked.")
    time.sleep(3)
    form = driver.find_element(By.ID, enter)
    if form:
        print("Enter button found.")
    else:
        print("Enter button NOT found.")
    form.submit()  # As this is a form, I focused on the form ID and not the button. Submit works well for this.
    print("Enter button clicked.")
    time.sleep(10)


try:
    driver.get(url)
    print("Website accessed!")
    time.sleep(5)
    apply_and_submit("ngxFrame270554", "xReturningUserEmail", "xCheckUser", "xSecondaryForm")
    print("HGTV Submitted.")
    time.sleep(10)
    food_link = driver.find_element(By.ID, "reentry-link")
    # https://www.hgtv.com/sweepstakes/hgtv-smart-home/sweepstakes/thanks is the link that should be clicked, not
    # working as it's not found.
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
