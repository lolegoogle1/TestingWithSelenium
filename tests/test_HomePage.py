from pageObjects.HomePage import HomePage
from utilities.Base import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self):
        home_page = HomePage(self.driver)

        home_page.get_name().send_keys("Oleh")
        home_page.get_email().send_keys("example")
        home_page.get_checkbox().click()
