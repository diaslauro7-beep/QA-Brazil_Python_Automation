import data
import helpers
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages import UrbanRoutesPage
import time

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert route_page.get_from_location_value() == data.ADDRESS_FROM
        assert route_page.get_to_location_value() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        # Nota: Verifique se route_page_click_confort_active() é um método de route_page
        assert route_page.route_page_click_confort_active()
        time.sleep(10)
        print("Testar seleção de plano")
        pass

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in route_page.numero_confirma()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
        assert "cartao" in route_page.confirm_cartao()


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.add_comment(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in route_page.confirm_cartao()
        time.sleep(10)

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.switch_cobertor()
        assert route_page.switch_cobertor_active() is True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        for _ in range(2):
            route_page.add_ice_creams()
        assert int(route_page.qnt_sorvete()) == 2



    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.click_number_text(data.PHONE_NUMBER)
        route_page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
        route_page.add_comment(data.MESSAGE_FOR_DRIVER)
        route_page.call_taxi()
        assert "buscar carro" in route_page.pop_up_show()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
