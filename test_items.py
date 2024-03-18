from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button) > 0, 'basket button not found'