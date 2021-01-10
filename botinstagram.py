from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\arthu\OneDrive\Área de Trabalho\geckodriver\geckodriver.exe')

    def login(self):  
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)

        '''Inserido usuário'''
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)

        '''inserindo senha'''
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)

        '''submetendo dados e confirmando login'''
        submit = self.driver.find_element_by_tag_name('form')
        submit.submit()

        try:
            """Fechando as notificações"""

            """Primeira etapa de confirmação"""
            notifications = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Agora não"]')))
            notifications.click()

            """Segunda etapa de confirmação"""
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Agora não"]'))).click()
        except NoSuchElementException:
            pass
    
    def abrir_perfil(self, usuario):
        try:
            self.driver.get('https://www.instagram.com/' + usuario + '/')
            time.sleep(1.5)
        except NoSuchElementException:
            print("Falha na busca")

    def abrir_primeira_foto(self):
        try:
            self.driver.find_element_by_xpath("//div[@class=\"eLAPa\"]").click()
            time.sleep(4)
        except NoSuchElementException:
            print("O Usuário não possui foto ou você não tem permissão.") 

    def proxima_foto(self):    
        botao_proximo = "//a[text()=\"Próximo\"]"        
        try:
            self.driver.find_element_by_xpath(botao_proximo).click()
            time.sleep(3)
            return True
        except NoSuchElementException:
            try:
                self.curtir_foto()
            except:
                pass
            print("- Usuário não possui mais fotos seguintes.")
            return False

    def curtir_sem_parar(self):
        self.abrir_primeira_foto()
        self.curtir_foto()
        while(True):
            prox_post = self.proxima_foto()
    
            if prox_post == True:
    
                """CURTIR FOTO"""
                self.curtir_foto()
                time.sleep(2)

                """BOTÃO PRÓXIMO"""
                self.proxima_foto()
                time.sleep(2)    
                
            else:
                print("- Não há mais fotos disponíveis para serem curtidas.")
                break

    def curtir_foto(self):
        curtir = self.driver.find_element_by_class_name('fr66n')
        soup = bs(curtir.get_attribute('innerHTML'),'html.parser')
        if(soup.find('svg')['aria-label'] == 'Curtir'):
            curtir.click()
        time.sleep(2)

    def fechar(self):
        time.sleep(4)
        self.driver.quit()

    def maximizar_janela(self):
        self.driver.maximize_window()

    def curtir_foto_by_qntd(self, qntd):
        self.abrir_primeira_foto()
        self.curtir_foto()
        i = 1
        while(i < qntd):
            self.proxima_foto()
            time.sleep(2)
            self.curtir_foto()
            i+=1      
