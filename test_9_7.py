from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_hover():
    driver=webdriver.Chrome()
    actions=ActionChains(driver)
    driver.get("https://the-internet.herokuapp.com/hovers")
    avatar=driver.find_element(By.XPATH,"//img[@src='/img/avatar-blank.jpg']")
    actions.move_to_element(avatar).perform()
    infor=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/users/1']")))
    assert "View profile" in infor.text
    print("Displaying infor")

def test_right_click():
    driver=webdriver.Chrome()
    actions=ActionChains(driver)
    driver.get("https://the-internet.herokuapp.com/context_menu")
    black_box=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='hot-spot']")))
    actions.context_click(black_box).perform()
    alert = driver.switch_to.alert
    assert "You selected a context menu" in alert.text
    print("Displaying alert")

def test_double_click():
    driver=webdriver.Chrome()
    actions=ActionChains(driver)
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    button=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//button[@ondblclick='myFunction()']")))
    actions.double_click(button).perform()
    alert=driver.switch_to.alert
    assert "You double clicked me.. Thank You.." in alert.text
    print("Displaying alert")

def test_click_hold():
    driver=webdriver.Chrome()
    actions=ActionChains(driver)
    driver.get("https://letcode.in/button")
    time.sleep(10)
    button=driver.find_element(By.XPATH,"//*[@text()='Button Hold']")
    print(button.text)

