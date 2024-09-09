from ui_automation.pages.login import Login
from ui_automation.pages.product import ProductPage
import pytest


def test_open_the_login_page(driver, load_page):
  l = Login(driver)
  l.login("standard_user", "secret_sauce")
  assert l.page_loaded(), "Page is not loaded correctly"


def test_add_item_to_the_cart(driver, load_page):
  l = Login(driver)
  l.login("standard_user", "secret_sauce")
  assert l.page_loaded(), "Page is not loaded correctly"
  p = ProductPage(driver)
  p.add_product()
  assert p.verify_the_cart_item()


@pytest.mark.world
@pytest.mark.parametrize("username_value, password_value, error_message", [
  ("standard_user", "test_123", "invalid_password"),
  ("test_user", "sauce_demo", "invalid_username"),
  ("locked_out_user", "secret_sauce", "locked_user")
], ids=["user_entered_invalid_password", "user_entered_invalid_username", "user_locked_out"])
def test_validate_user_login(driver, load_page, username_value, password_value, error_message):
  l = Login(driver)
  l.login(username_value, password_value)
  assert l.get_error_message() == l.errors_messages(error_message)
