import pytest


from pages.login import Login
from pages.product import ProductPage


def test_open_the_login_page(driver):
  l = Login(driver)
  l.loadPage()
  l.login("standard_user", "secret_sauce")
  assert l.page_loaded(), "Page is not loaded correctly"


def test_add_item_to_the_cart(driver):
  l = Login(driver)
  l.loadPage()
  l.login("standard_user", "secret_sauce")
  assert l.page_loaded(), "Page is not loaded correctly"
  p = ProductPage(driver)
  p.add_product()
  assert p.verify_the_cart_item()