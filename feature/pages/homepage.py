import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    PAGE_URL = "https://www.saucedemo.com/"

    text_fields = {
        "Username": (By.ID, "user-name"),
        "Password": (By.ID, "password"),
        "firstname": (By.ID, "first-name"),
        "lastname": (By.ID, "last-name"),
        "zip": (By.ID, "postal-code"),
    }

    navigation_buttons = {
        "Login": (By.ID, "login-button"),
        "Cart": (By.CLASS_NAME, "shopping_cart_link"),
        "Checkout":(By.CLASS_NAME, "checkout_button"),
        "Continue":(By.ID, "continue"),
        "ContinueShopping":(By.ID, "continue-shopping"),
        "Finish":(By.ID, "finish"),
        "Menu":(By.ID, "react-burger-menu-btn"),
        "Logout":(By.ID, "logout_sidebar_link"),
    }

    item_cart_buttons = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
    }
    item_remove_buttons = {
        "Sauce Labs Backpack": (By.ID, "remove-sauce-labs-backpack"),
        "Sauce Labs Bike Light": (By.ID, "remove-sauce-labs-bike-light"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "remove-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Fleece Jacket": (By.ID, "remove-sauce-labs-fleece-jacket"),
        "Sauce Labs Onesie": (By.ID, "remove-sauce-labs-onesie"),
    }

    messages = {
        "Login Error": (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3"),
        "Checkout Error": (By.CSS_SELECTOR, ".error-message-container > h3"),
        "Top item":(By.CSS_SELECTOR, ".inventory_item_name")
    }

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def close_page(self):
        self.driver.quit()

    def fill_out_field(self, field, text):
        self.driver.find_element(*self.text_fields[field]).send_keys(text)

    def click_button(self, button):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(*self.navigation_buttons[button]))).click()
        #self.driver.find_element(*self.navigation_buttons[button]).click()
    
    def click_option_button(self, option):
        dropdown  = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        select = Select(dropdown)
        select.select_by_value(option)
    def click_item_cart_button(self, item):
        self.driver.find_element(*self.item_cart_buttons[item]).click()
    def click_item_remove_button(self, item):
        self.driver.find_element(*self.item_remove_buttons[item]).click()

    def get_error_message(self):
        return self.driver.find_element(*self.messages["Login Error"]).text
    def get_error_message_checkout(self):
        return self.driver.find_element(*self.messages["Checkout Error"]).text
    def get_top_item_name(self):
        return self.driver.find_element(*self.messages["Top item"]).text
    def get_current_url(self):
        parsed_url = urlparse(self.driver.current_url)
        path = parsed_url.path
        return path.lstrip('/')
    def get_current_url_full(self):
        return self.driver.current_url
    def get_cart_count(self):
        try:
            count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        except selenium.common.exceptions.NoSuchElementException:
            return '0'

        return count