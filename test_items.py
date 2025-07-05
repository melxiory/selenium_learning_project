#link = "http://selenium1py.pythonanywhere.com/"
import time

from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    #time.sleep(5)
    basket = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert basket, 'Ошибка, кнопки Добавить нет'
