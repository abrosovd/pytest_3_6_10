import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    button_elements = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(button_elements) == 1, f"Found {str(len(button_elements))} buttons instead of 1"
    time.sleep(5)