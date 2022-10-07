import utilXL
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.stealmylogin.com/demo.html/")
driver.maximize_window()
file = "./hello_world.xlsx"

rows = utilXL.get_row_count(file, "Sheet")
for r in range(2, rows+1):
    username = utilXL.read_data(file, "Sheet", r, 1)
    password = utilXL.read_data(file, "Sheet", r, 2)
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("type", "submit").click()
