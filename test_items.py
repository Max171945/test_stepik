import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_get_button_add_to_basket(browser):

    """ The test verifies that the page contains an add to basket button """

    browser.get(link)
    #time.sleep(30)
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert button, "The button does not exist"


