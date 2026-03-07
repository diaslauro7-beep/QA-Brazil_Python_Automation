import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Tarifa chamar taxi
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"Taxi")]')
    confort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    confort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[5]')

    # Numero de Telefone
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_conform = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confir = (By.XPATH, '//button[contains(text(),"confirma")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # Metodo de Pagamento
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"adicionar")]')
    closed_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    corfirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    add_comment = (By.ID, 'comment')

    # LENÇOS E COBERTOR

    swith_blanket = (By.CSS_SELECTOR, 'switch')
    swith_blanket_active = (By.CSS_SELECTOR,
                            '.r-type-switch-input')

    # PEDIR SORVETES

    add_icecream = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')

    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-heador-title')


    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_texte):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_texte)

    def enter_to_location(self, to_texte):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_texte)

    def enter_location(self, from_texte, to_texte):
        self.enter_from_location(from_texte)
        self.enter_to_location(to_texte)

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_field)).get_attribute('value')

    def click_taxi_option(self):
        self.driver.find_element(*self.taxi_option_locator).click()

    def click_confort_icon(self):
        self.driver.find_element(*self.confort_icon_locator).click()

    def click_confort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.confort_active))
            return "active" in active_button.get_attribute("class")
        except:
            return False

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.from_field)).get_attribute('value')


    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()
        self.driver.find_element(*self.number_enter).send_keys(telefone)
        self.driver.find_element(*self.number_conform).click()

        # Recuperação do código via helper
        code = retrieve_phone_code(self.driver)

        code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number_code))
        code_input.clear()
        code_input.send_keys(code)
        self.driver.find_element(*self.code_confir).click()

    def numero_confirmado(self):
        numero = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number_finish))
        return numero.text

    def click_add_cartao(self, card_number, card_code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        input_card = self.driver.find_element(*self.number_card)
        input_card.send_keys(card_number)
        input_card.send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, 'code').send_keys(card_code)
        self.driver.find_element(By.NAME, 'code').send_keys(Keys.TAB)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.closed_button_card).click()

    def confirm_cartao(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.corfirm_card)).text

    def set_comment(self, comment):
        self.driver.find_element(*self.add_comment).send_keys(comment)

    def toggle_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.switch_blanket).click()

    def add_ice_creams(self, quantity):
        plus_button = self.driver.find_element(*self.add_icecream)
        for _ in range(quantity):
            plus_button.click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.qnt_icecream).text


    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def get_order_header_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.pop_up)).text




