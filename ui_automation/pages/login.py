from pages.search import SearchPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login(SearchPage):
  USERNAME = (By.ID, 'user-name')
  PASSWORD = (By.ID, 'password')
  LOGIN_BUTTON = (By.ID, "login-button")
  SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

  def __init__(self, driver):
    super().__init__(driver)

  def login(self, username_value, password_value):
    username = self.driver.find_element(*self.USERNAME)
    username.send_keys(username_value)

    password = self.driver.find_element(*self.PASSWORD)
    password.send_keys(password_value)
    self.driver.find_element(*self.LOGIN_BUTTON).click()
    time.sleep(3)

  def page_loaded(self):
    element = self.driver.find_element(*self.SHOPPING_CART)
    return element.is_displayed()
