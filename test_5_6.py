from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")
    time.sleep(4)
def test_case1():
    driver=webdriver.Chrome()
    test_login(driver)
    Alert = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='fw-semibold']")))
    assert "Failed to publish the portfolio. Please check the following errors." in Alert.text,f"No Error msg alert"
    print(f"Exist Error msg alert:{Alert.text}")
    try:
        Msg_error = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='_node-key-link_1rpzv_25 text-decoration-none ms-1']")))
        print(f"Exist Error campaign:{Msg_error.text}")
    except:
        print("Not exist error campaign")
    driver.quit()
def test_case2():
    driver = webdriver.Chrome()
    test_login(driver)
    filter_1 = WebDriverWait(driver,5).until(EC.visibility_of_element((By.XPATH, "//div[@class='_select_19ily_1 css-ll793-control']")))
    filter_1.click()
    dropdownEl = WebDriverWait(driver,5).until(EC.visibility_of_element((By.XPATH, "//span[@data-at_id='select__multi_icontains']")))
    dropdownEl.click()
    input_filter_1 = WebDriverWait(driver,5).until(EC.visibility_of_element((By.XPATH, "//input[@id='textSearch1']")))
    input_filter_1.send_keys("Adgr")
    input_filter_2 = WebDriverWait(driver,5).until(EC.visibility_of_element((By.XPATH, "//input[@id='textSearch2']")))
    input_filter_2.send_keys("1237")
    btn_apply = driver.find_element(By.XPATH,"//button[@data-at_id='btn__search_apply']")
    scroll = ActionChains(driver)
    scroll.move_to_element(btn_apply).perform()
    WebDriverWait(driver,5)
    btn_apply.click()
    MatchRecord=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='_preview-card_8o8n8_19']")))
    scroll.move_to_element(MatchRecord).perform()
    assert "Adgr" in MatchRecord.text and "1237" in MatchRecord.text, f"No matching record"
    print(f"Exist matching record ")

def test_case5():
    driver = webdriver.Chrome()
    test_login(driver)
    BtnEditPF=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-at_id='btn__portfolio_detail']"))).click()
    try:
      PopupEditPF=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div[@data-at_id='modal__create_new_portfolio']")))
      print("Can open portfolio edit popup")
    except:
        print("Can not open portfolio edit popup")
    BtnClose=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//button[@data-at_id='btn__close_create_new_portfolio']"))).click()
    print("Close popup")
    driver.quit()

# def test_case6():
#     driver=webdriver.Chrome()
#     test_login(driver)
#     num_of_records = 0
#     rows = driver.find_element(By.XPATH)

def test_case8():
    driver=webdriver.Chrome()
    test_login(driver)
    checkbox1=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//td[@data-at_id='td__table_rsa_select_2840']")))
    checkbox2=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//td[@data-at_id='td__table_rsa_select_2838']")))
    scroll=ActionChains(driver)
    scroll.move_to_element(checkbox2).perform()
    checkbox1.click()
    checkbox2.click()
    btn_overwrite=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-at_id='btn__bulk_overwrite_header_table_action']")))
    assert "Bulk Overwrite" in btn_overwrite.text, f"not appear button"
    print("appear button")

def test_case9():
    driver=webdriver.Chrome()
    test_login(driver)
    page1=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//li[@class='page-item active']")))
    record_of_page1=
    scroll=ActionChains(driver)
    scroll.move_to_element(page1).perform()
    page2=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@aria-label='Go to page 2']")))
    assert "2" in page2.text, f"No exist page 2"
    page2.click()
    time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test_case9()