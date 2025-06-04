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
userName.send_keys("admin")
time.sleep(2)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("SP@123456")
time.sleep(2)
btnlogin = driver.find_element(By.XPATH, "//button[@type='submit']")
btnlogin.click()
time.sleep(2)
# Đi tới màn hình list RSA
driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")
time.sleep(10)
try:
    # Chờ thông báo lỗi xuất hiện (tối đa 5 giây)
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Failed to publish the portfolio. Please check the following errors.')]")
        )
    )

    assert error_message.is_displayed()
    print("✅ Tồn tại banner.")
except:
    print("❌ Không tồn tại Banner.")
finally:
    driver.quit()