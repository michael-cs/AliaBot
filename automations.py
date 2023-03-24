from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import os
# import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


class Tasks():
    def __init__(self, url, email, password, barcode, titulo, nome, marca,
                 peso, empresa, descricao):
        self.url = url
        self.email = email
        self.password = password
        self.barcode = barcode
        self.titulo = titulo
        self.nome = nome
        self.marca = marca
        self.peso = peso
        self.empresa = empresa
        self.descricao = descricao

    def AbrePainelAlia(url):
        driver.implicitly_wait(10)
        driver.get(url)

    def EfetuaLogin(email, password):
        email_field = driver.find_element(
            By.XPATH, "//input[@placeholder='Email']")

        password_field = driver.find_element(
            By.XPATH, "//input[@placeholder='Password']")

        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")

        driver.implicitly_wait(10)

        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()

    @staticmethod
    def AbreCadastroDeProdutos():
        driver.implicitly_wait(10)
        produtos_button = driver.find_element(
            By.XPATH, "//p[normalize-space()='Produtos']")
        produtos_button.click()
        adicionar_button = driver.find_element(
            By.XPATH, "//a[@class='btn btn-sm btn-primary']")
        adicionar_button.click()

    @staticmethod
    def InsereImagem():
        driver.implicitly_wait(10)
        adicionarimagem_button = driver.find_element(
            By.XPATH, "//input[@name='medias[]']")
        path = os.path.abspath('./logoAlia.jpg')
        adicionarimagem_button.send_keys(path)

    def PreencheCampos(barcode, titulo, nome, marca, peso, empresa, descricao):

        codigo_de_barras_campo = driver.find_element(
            By.XPATH, "//input[@id='input-barcode']")
        titulo_campo = driver.find_element(
            By.XPATH, "//input[@id='input-title']")
        nome_produto_campo = driver.find_element(
            By.ID, 'input-name')
        marca_do_produto_campo = driver.find_element(
            By.XPATH, "//input[@id='input-brand']")
        peso_produto_campo = driver.find_element(
            By.XPATH, "//input[@id='input-weight']")
        empresa_campo = Select(driver.find_element(
            By.ID, "input-company"))
        cadastrar_button = driver.find_element(
            By.XPATH, "//button[@type='submit']")
        text_area = driver.find_element(
            By.XPATH, "//div[@class='tox-toolbar__primary']")
        description_area = driver.find_element(By.ID, "input-description_ifr")

        codigo_de_barras_campo.send_keys(barcode)
        codigo_de_barras_campo.send_keys(Keys.TAB)
        titulo_campo.send_keys(titulo)
        titulo_campo.send_keys(Keys.TAB)
        nome_produto_campo.send_keys(nome)
        nome_produto_campo.send_keys(Keys.TAB)
        marca_do_produto_campo.send_keys(marca)
        marca_do_produto_campo.send_keys(Keys.TAB)
        peso_produto_campo.send_keys(peso)
        peso_produto_campo.send_keys(Keys.TAB)
        empresa_campo.select_by_visible_text(empresa)
        text_area.click()
        driver.execute_script("tinyMCE.activeEditor.setContent('{}')"
                              .format(descricao))
        description_area.send_keys(Keys.TAB)
        cadastrar_button.click()

    @staticmethod
    def CloseBrowser():
        driver.quit
