import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Localizadores de Endereço
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Seleção de Plano/Taxi
    taxi_option_locator = (By.CSS_SELECTOR, "button.button.round")
    confort_icon_locator = (By.XPATH, "//div[text()='Comfort']/parent::div")
    confort_active_locator = (By.XPATH, "//div[text()='Comfort']/ancestor::div[contains(@class, 'active')]")

    # Telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm_btn = (By.XPATH, '//button[text()="Confirmar"]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # Pagamento
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.NAME, 'code')
    add_finish_card = (By.XPATH, '//button[text()="Adicionar"]')
    closed_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card_text = (By.CSS_SELECTOR, '.pp-value-text')

    # Comentário e Extras
    add_comment_field = (By.ID, 'comment')
    switch_blanket = (By.CSS_SELECTOR, '.r-type-switch')
    switch_blanket_input = (By.CSS_SELECTOR, '.r-type-switch-input')

    # Sorvete
    add_icecream_btn = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream_val = (By.CSS_SELECTOR, '.counter-value')

    # Finalização
    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def enter_location(self, from_text, to_text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field)).send_keys(from_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.to_field)).send_keys(to_text)

    def get_from_location_value(self):
        return self.driver.find_element(*self.from_field).get_attribute('value')

    def get_to_location_value(self):
        return self.driver.find_element(*self.to_field).get_attribute('value')

    def click_taxi_option(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.taxi_option_locator)).click()

    def click_confort_icon(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confort_icon_locator)).click()

    def is_comfort_active(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.confort_active_locator)
            )
            return True
        except:
            return False

    def fill_phone_number(self, phone):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.number_text_locator)).click()
        self.driver.find_element(*self.number_enter).send_keys(phone)
        self.driver.find_element(*self.number_confirm).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.number_code).send_keys(code)
        self.driver.find_element(*self.code_confirm_btn).click()

    def get_phone_number_text(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.number_finish)).text

    def add_credit_card(self, card_number, card_code):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_metodo_pagamento)).click()
        self.driver.find_element(*self.add_card).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.number_card)).send_keys(card_number)
        self.driver.find_element(*self.code_card).send_keys(card_code)
        self.driver.find_element(*self.code_card).send_keys(Keys.TAB)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.closed_button_card).click()

    def get_card_status_text(self):
        return self.driver.find_element(*self.confirm_card_text).text

    def set_comment(self, comment):
        self.driver.find_element(*self.add_comment_field).send_keys(comment)

    def get_comment_value(self):
        return self.driver.find_element(*self.add_comment_field).get_attribute('value')

    def toggle_blanket(self):
        self.driver.find_element(*self.switch_blanket).click()

    def is_blanket_active(self):
        return self.driver.find_element(*self.switch_blanket_input).is_selected()

    def add_ice_creams(self, quantity):
        plus_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_icecream_btn)
        )
        for _ in range(quantity):
            plus_button.click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.qnt_icecream_val).text

    def call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def get_order_title(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.pop_up)).text