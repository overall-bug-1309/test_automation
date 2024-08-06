import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def driver():
  service = Service(ChromeDriverManager().install())
  #Initialize the driver

  driver = selenium.webdriver.Chrome(service=service)
  driver.maximize_window()
  driver.implicitly_wait(5)

  #Return the driver
  yield driver

  #Quit the driver once the usage is done
  driver.quit()