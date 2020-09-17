from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_button_add_to_cart(browser):

    browser.get(link)
    assert browser.find_elements(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'), 'Нет кнопки добавления в корзину'
