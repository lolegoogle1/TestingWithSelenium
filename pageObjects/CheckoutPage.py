from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//button[@class='btn btn-success]")

    def __init__(self, driver):
        self.driver = driver

    def get_card_titles(self):
        return self.driver.find_element(*CheckoutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_element(*CheckoutPage.card_footer)

    def checkout_items(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page