import time

from ui_automation.pages.login import Login
from selenium.webdriver.common.by import By


class ProductPage(Login):
  product_1 = (By.ID, 'item_4_title_link')
  product_1_name = "Sauce Labs Backpack"
  add_product_1 = (By.ID, "add-to-cart-sauce-labs-backpack")
  cart_product_1 = (By.ID, "item_4_title_link")

  def __init__(self, driver):
    super().__init__(driver)

  def add_product(self):
    product = self.driver.find_element(*self.product_1)
    c = product.text
    if product.text == self.product_1_name:
      self.driver.find_element(*self.add_product_1).click()
    else:
      print('Product not available')

  def verify_the_cart_item(self):
    self.driver.find_element(*self.SHOPPING_CART).click()
    time.sleep(4)
    c = self.driver.find_element(*self.cart_product_1).text
    if self.driver.find_element(*self.cart_product_1).text == self.product_1_name:
      return bool(True)
