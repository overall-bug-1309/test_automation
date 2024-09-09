from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage():
  def __init__(self, driver):
    self.driver = driver

