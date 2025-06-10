from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login(driver):

    # Khoi tao trinh duyet
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
    time.sleep(10)
def test_case1():
    driver=webdriver.Chrome()
    test_login(driver)
    alert=driver.find_element(By.XPATH, "//span[@class='fw-semibold']")
    assert "Failed to publish the portfolio. Please check the following errors." in alert.text, f"Not exist alert"
    print("Exist alert")
    try:
        error_msg=driver.find_element(By.XPATH, "//span[@class='_node-key-msg_1rpzv_21 ms-1']")
        assert "エラーを必要な形式に変換できません。オリジナルのタブを参照してください。" in error_msg.text, f"Error message not display"
    except: 
        print("Exist error message")
def test_case2():
    driver=webdriver.Chrome()
    test_login(driver)
    filter1=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='d-flex align-items-center justify-content-center']")))
    filter1.click()
    time.sleep(3)
    option1=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-at_id='select__multi_icontains']")))
    option1.click()
    searchbox1=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='textSearch1']")))
    searchbox1.send_keys("Adgr")
    searchbox2=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='textSearch2']")))
    searchbox2.send_keys("1237")
    time.sleep(10)
    


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test_case2()

