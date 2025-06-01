'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao trinh duyet
driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
time.sleep(1)'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao trinh duyet
driver = webdriver.Chrome()
driver.get("https://dev.sp.leadplus.net/login")
driver.maximize_window()
time.sleep(2)
# Tim phan tu
userName = driver.find_element(By.XPATH, "//input[@name='username']")
userName.send_keys("admin")
time.sleep(2)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("SP@123456")
time.sleep(2)
btnlogin = driver.find_element(By.XPATH, "//button[@type='submit']")
btnlogin.click()
time.sleep(180)