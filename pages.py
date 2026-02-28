from asyncio import timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

     def enter_from_location(self, from_texte):
         self.driver.field_element(*self.from_field).send_keys(from_texte)

    def enter_to_location(self, to_texte):
        self.driver.field_element(*self.to_field).send_keys(to_texte)

    def entre_location(self, from_texte, to_texte):
        self.enter_from_location(from_texte)
        self.enter_to_location(to_texte)

    def get_to_location_value(self):
      return WebDriverWait(self.driver, 3).until(
          EC.visibility_of_element_located(self.to_field)).get_attribute('value')