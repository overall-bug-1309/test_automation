from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage():
  URL = "https://www.saucedemo.com/"

  def __init__(self, driver):
    self.driver = driver

  def loadPage(self):
    self.driver.get(self.URL)
