from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Github credential
# username = "username"
# password = "password"
username = "student1"
password = "Password123"
# initial the chrom driver
driver = webdriver.Chrome()

# head to github login page
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# click on login buttom
driver.find_element(By.ID, "submit").click()

# wait the ready state to the complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

error_messages = "Your username is invalid!"

errors = driver.find_element(By.ID, "error")

driver.close()
driver.quit()