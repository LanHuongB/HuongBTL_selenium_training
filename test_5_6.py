from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khoi tao trinh duyet
driver = webdriver.Chrome()
driver.get("https://dev.sp.leadplus.net/login")
driver.maximize_window()
time.sleep(2)
# Tim phan tu
userName = driver.find_element(By.XPATH, "//input[@name='username']")
userName.send_keys("huongbtl@liftsoft.vn")
time.sleep(2)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("SP@123456")
time.sleep(2)
btnlogin = driver.find_element(By.XPATH, "//button[@type='submit']")
btnlogin.click()
time.sleep(2)
# Đi tới màn hình list RSA
driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")
time.sleep(2)
Alert = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='fw-semibold']")))
assert "Failed to publish the portfolio. Please check the following errors." in Alert.text, f"Không tìm thấy Error msg alert"
print(f"Đã tìm thấy Error msg alert:{Alert.text}")
try:
    Msg_error = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='_node-key-link_1rpzv_25 text-decoration-none ms-1']")))
    print(f"Tồn tại campaign lỗi:{Msg_error.text}")
except:
    print("Không tồn tại campaign lỗi")
driver.quit()