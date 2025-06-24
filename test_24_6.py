from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_login(driver):
    driver.get("https://dev.sp.leadplus.net/")
    driver.maximize_window()
    username=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    password=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
    login_btn=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-at_id='btn__login']")))
    username.send_keys("huongbtl@liftsoft.vn")
    password.send_keys("SP@123456")
    login_btn.click()
    time.sleep(5)
    driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")

def test_bai1():
    driver=webdriver.Chrome()
    test_login(driver)
    allert=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='fw-semibold']")))
    msg_error=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-at_id='msg__publish_status_alert']")))
    assert "Failed to publish the portfolio. Please check the following errors."in allert.text, f"Khong xuat hien allert"
    print("Xuat hien alert")
    try:
        assert "15113_GGS (can create RSA/ KW/ Negative KW)" in msg_error.text
        print("Xuat hien ma loi 15113_GGS (can create RSA/ KW/ Negative KW)")
    except:
        print("Khong xuat hien ma loi 15113_GGS (can create RSA/ KW/ Negative KW)")
    time.sleep(5)

def test_bai2():
    driver=webdriver.Chrome()
    test_login(driver)
    search_filter1=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class=' css-hlgwow']")))
    search_filter1_input=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='textSearch1']")))
    search_filter1.click()

    # search_filter2_input=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='textSearch2']")))
    filter1_option=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-at_id='select__multi_icontains']")))
    filter1_option.click()
    apply_btn=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-at_id='btn__search_apply']")))
    search_filter1_input.send_keys("Adgr")
    apply_btn.click()
    time.sleep(5)


