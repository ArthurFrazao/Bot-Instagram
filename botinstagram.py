from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\arthu\OneDrive\Área de Trabalho\geckodriver\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(6)
        driver.find_element_by_xpath('//button[text()="Salvar informações"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//button[text()="Agora não"]').click()     
        time.sleep(2)    
        #self.curtir_fotos('memesbr')
        self.stalkear('sr.frazao')


    def stalkear(self, usuario):
        driver = self.driver
        driver.get('https://www.instagram.com/' + usuario + '/')
        time.sleep(2)
        for i in range(0, 2):
            # CADA LINHA NO NAVEGADOR EQUIVALE A 11 LINES
            driver.execute_script("window.scrollByLines(11)")
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if usuario in href]

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollByLines(1)")
            try:
                driver.find_element_by_xpath('//button[text()="Curtir"]').click()
                driver.find_element_by_xpath('//button[text()="Próximo"]').click()
                time.sleep(6)
            except Exception as e:
                time.sleep(5)

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)
        for i in range(0, 2):
            # CADA LINHA NO NAVEGADOR EQUIVALE A 11 LINES
            driver.execute_script("window.scrollByLines(11)")
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos:  ' + str(len(pic_hrefs)))
        
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollByLines(1)")
            try:
                driver.find_element_by_xpath('//button[text()="Curtir"]').click()
                time.sleep(10)
            except Exception as e:
                time.sleep(5)
    

arthurbot = InstagramBot('zezediluciano', 'snake2.0') 
arthurbot.login()
