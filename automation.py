from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Firefox options (optional)
firefox_options = Options()
# firefox_options.add_argument('--headless')  # Uncomment to run in headless mode

# Initialize the Firefox driver
driver = webdriver.Firefox(options=firefox_options)

try:
    # Opens Our Website
    print("Opening Firefox and navigating to Google...")
    driver.get("https://catalystprogrammers.in")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Courses']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Enroll Now']").click()
    time.sleep(3)

    # Opens YouTube
    print("Opening Firefox and navigating to YouTube...")
    driver.get("https://www.youtube.com/@lyfofvipin_tech")
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[text()='Live']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[text()='Playlists']").click()
    time.sleep(10)
finally:
    print("Closing browser...")
    driver.quit()
