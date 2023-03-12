from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



capabilities = webdriver.DesiredCapabilities.CHROME
print(capabilities)

# initialize desire webdriver
driver = webdriver.Chrome(desired_capabilities=capabilities)
driver.get("https://www.tiktok.com/signup/phone-or-email/phone")

# # click sign up button
# login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/button")
# login_button.click()

# sign_up_button = driver.find_element(By.XPATH, "//a[@href='/signup/phone-or-email/phone']")
# sign_up_button.click()

# phone_or_email_button = driver.find_element(By.XPATH, "//a[@href='/signup/phone-or-email/phone']")
# phone_or_email_button.click()