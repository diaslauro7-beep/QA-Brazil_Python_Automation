import data
import helpers
from asyncio import timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")



    def test_set_route(self):
     self.driver.get(data.URBAN_ROUTES_URL)
     route_page = UrbanRoutesPage(self.driver)
     route_page.enter_location(data.ADDRESS_FROM , data.ADDRESS_TO)
    assert routes_page.get_from_location_value() == data.ADDRESS_FROM
    assert routes_page.get_from_location_value() == data.ADDRESS_TO


    def test_select_plan(self):
      # Adicionar em S8
      print("Testar seleção de plano")
      pass

    def test_fill_phone_number(self):
      # Adicionar em S8
      print("Testar preenchimento do telefone")
      pass

    def test_fill_card(self):
      # Adicionar em S8
      print("Testar preenchimento do cartão")
      pass

    def test_comment_for_driver(self):
      # Adicionar em S8
      print("Testar comentário para o motorista")
      pass

    def test_order_blanket_and_handkerchiefs(self):
      # Adicionar em S8
      print("Testar pedido de cobertor e lenços")
      pass

    def test_order_2_ice_creams(self):
      # Adicionar em S8
      numbers_of_ice_creams= 2
      for count in range(numbers_of_ice_creams):
       print("Testar pedido de 2 sorvetes")
      pass

    def test_car_search_model_appears(self):
      # Adicionar em S8
      print("Testar se modelo do carro aparece na busca")
      pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()