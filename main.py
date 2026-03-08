import data
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = Chrome(options=options)
        cls.driver.implicitly_wait(10)

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
        assert route_page.is_comfort_active() is True

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.fill_phone_number(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in route_page.get_phone_number_text()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartão" in route_page.get_card_status_text()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_comment(data.MESSAGE_FOR_DRIVER)
        assert route_page.get_comment_value() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.toggle_blanket()
        assert route_page.is_blanket_active() is True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.add_ice_creams(2)
        assert route_page.get_ice_cream_count() == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        route_page = UrbanRoutesPage(self.driver)
        route_page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        route_page.click_taxi_option()
        route_page.click_confort_icon()
        route_page.fill_phone_number(data.PHONE_NUMBER)
        route_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        route_page.call_taxi()
        assert "Buscar carro" in route_page.get_order_title()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()