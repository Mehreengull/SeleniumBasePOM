from pages.loginPage import LoginPage
from seleniumbase import BaseCase


class MyTest(BaseCase):
    def test(self):
        LoginPage().test_login(self, "tomsmith", "SuperSecretPassword!")
        self.assert_element("//h2[normalize-space()='Secure Area']")
