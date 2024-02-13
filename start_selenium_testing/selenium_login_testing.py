from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd


def users_credentials():
    data = pd.read_excel('./username_password.xlsx')
    usernames = data["Username"].tolist()
    passwords = data["Password"].tolist()
    credentials = []
    for i in range(len(usernames)):
        credentials.append({
            "username": usernames[i],
            "password": passwords[i]
        })

    return credentials


# Load chrome web driver
driver = webdriver.Chrome()


for user in users_credentials():
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys(user.get("username"))
    driver.find_element(By.ID, "password").send_keys(user.get("password"))

    # click on login button
    driver.find_element(By.ID, "submit").click()

    # wait the ready state to the complete
    WebDriverWait(driver=driver, timeout=5).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    try:
        errors = driver.find_element(By.ID, "error")
        print(errors.text)
    except Exception as e:
        success_message = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/p[1]/strong')
        print(success_message.text)

    # driver.find_element(By.ID, "username").clear()
    # driver.find_element(By.ID, "password").clear()

driver.quit()
