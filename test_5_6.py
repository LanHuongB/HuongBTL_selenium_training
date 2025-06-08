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
    # Đi tới màn hình list RSA
    driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")
    time.sleep(4)
def test_case1():
    driver=webdriver.Chrome()
    test_login(driver)
    Alert = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='fw-semibold']")))
    assert "Failed to publish the portfolio. Please check the following errors." in Alert.text, f"Không tìm thấy Error msg alert"
    print(f"Đã tìm thấy Error msg alert:{Alert.text}")
    try:
        Msg_error = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='_node-key-link_1rpzv_25 text-decoration-none ms-1']")))
        print(f"Tồn tại campaign lỗi:{Msg_error.text}")
    except:
        print("Không tồn tại campaign lỗi")
    driver.quit()
def test_case2():
    driver = webdriver.Chrome()
    test_login(driver)
    filter_1 = driver.find_element(By.XPATH, "//div[@class='_select_19ily_1 css-ll793-control']")
    filter_1.click()
    time.sleep(1)
    dropdownEl = driver.find_element(By.XPATH, "//span[@data-at_id='select__multi_icontains']")
    dropdownEl.click()
    time.sleep(1)
    input_filter_1 = driver.find_element(By.XPATH, "//input[@id='textSearch1']")
    input_filter_1.send_keys("Adgr")
    time.sleep(1)
    input_filter_2 = driver.find_element(By.XPATH, "//input[@id='textSearch2']")
    input_filter_2.send_keys("1237")
    time.sleep(3)
    btn_apply = driver.find_element(By.XPATH,"//button[@data-at_id='btn__search_apply']")
    scroll = ActionChains(driver)
    scroll.move_to_element(btn_apply).perform()
    WebDriverWait(driver,5)
    btn_apply.click()
    MatchRecord=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='_preview-card_8o8n8_19']")))
    scroll.move_to_element(MatchRecord).perform()
    assert "Adgr" in MatchRecord.text and "1237" in MatchRecord.text, f"Không thể tìm thấy record matching"
    print(f"Đã tìm thấy record matching chứa KW search Adgr và 1237 ")

def test_case5():
    driver = webdriver.Chrome()
    test_login(driver)
    BtnEditPF=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-at_id='btn__portfolio_detail']"))).click()
    try:
      PopupEditPF=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div[@data-at_id='modal__create_new_portfolio']")))
      print("Có thể mở popup edit portfolio")
    except:
        print("Không thể mở popup edit portfolio")
    BtnClose=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//button[@data-at_id='btn__close_create_new_portfolio']"))).click()
    print("Đã đóng popup")
    driver.quit()

def test_case10():
    driver = webdriver.Chrome()
    test_login(driver)
    apr_status=driver.find_element(By.XPATH, "//input[@id='react-select-14-input']")
    apr_status.click()
    time.sleep(2)
    status=driver.find_element(By.XPATH, "//span[@class='mx-2 d-flex align-items-center justify-content-between gap-1 pointer']")
    status.click()
    time.sleep(10)
    rows = driver.find_elements(By.XPATH, "//table//tr[position()>1]")  # bỏ header
    all_ok = True  # biến để theo dõi trạng thái
    for index, row in enumerate(rows, start=1):
        try:
            status_cell = row.find_element(By.XPATH, "./td[5]")  # cột thứ 5 là "Approval Status"
            status_text = status_cell.text.strip()
            if status_text != "Not published":
                print(f"Row {index} có Approval Status khác: '{status_text}'")
                all_ok = False
            else:
                print(f"Row {index} OK: Approval Status = 'Not published'")
        except Exception as e:
            print(f"Row {index} bị lỗi khi đọc dữ liệu: {e}")
            all_ok = False

assert all_ok, "Một hoặc nhiều dòng có Approval Status khác 'Not published'"
print("Tất cả các dòng đều có Approval Status = 'Not published'")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test_case10()

