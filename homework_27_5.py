from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
time.sleep(1)