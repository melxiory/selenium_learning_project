from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    # GIVEN
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()



    num = browser.find_element(By.ID, 'input_value').text
    result = math.log(abs(12*math.sin(float(num))))



    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(result)

    answer_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    answer_button.click()


finally:
    time.sleep(10)
    browser.quit()
