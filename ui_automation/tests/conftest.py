import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
  parser.addoption("--browser", action="store", default="Chrome", help="Enter browser of your choice")
  parser.addoption("--headless", action="store_true", help="This will run the test in hidden mode")


@pytest.fixture()
def browser(request):
  return request.config.getoption("--browser")


@pytest.fixture()
def headless(request):
  return request.config.getoption("--headless")


@pytest.fixture()
def driver(browser):
  global driver

  if browser == "Firefox":
    service = FirefoxService(GeckoDriverManager().install())
    driver = selenium.webdriver.Firefox(service=service)
  else:
    service = ChromeService(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=service)

  #Initialize the driver

  driver.maximize_window()
  driver.implicitly_wait(5)

  #Return the driver
  yield driver

  #Quit the driver once the usage is done
  driver.quit()


@pytest.fixture
def load_page(driver):
  url = "https://www.saucedemo.com/"
  driver.get(url)
