import pytest

from selenium import webdriver



from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.Base import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()
        cards = checkout_page.get_card_titles()

        for index, card in enumerate(cards):
            card_text = card.text
            print(card_text)

            if card_text == "Blackberry":
                checkout_page.get_card_footer()[index].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirm_page = checkout_page.checkout_items()

        self.driver.find_element_by_id("country").send_keys("ind")

        element = self.verify_link_presence("India")


        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        text_match = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        assert "Success! Thank you!" in text_match
