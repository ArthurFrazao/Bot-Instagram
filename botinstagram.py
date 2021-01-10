from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time, getpass

# Add your path geckodriver
driver = webdriver.Firefox(executable_path=r'C:...')

class InstagramBot:
    def __init__(self):
        self.driver = driver  
        self.maximize_window()      
        self.login()        

    def login(self):  
        user = input("Nome de usuario: ")   
        password = getpass.getpass("Senha: ") 
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)

        #insert username             
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(user)
        
        #insert password          
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)

        #submit login
        submit = self.driver.find_element_by_tag_name('form')
        submit.submit()

        #close notification
        try:            
            #1st pop-up            
            notifications = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Agora não"]')))
            notifications.click()

            #2nd pop-up
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Agora não"]'))).click()
        except NoSuchElementException:
            pass
        
    def open_profile(self):
        profile = input("Perfil: ")
        try:
            self.driver.get('https://www.instagram.com/' + profile + '/')
            time.sleep(1.5)
        except NoSuchElementException:
            print("Falha na busca")

    def open_1st_pic(self):
        try:
            self.driver.find_element_by_xpath("//div[@class=\"eLAPa\"]").click()
            time.sleep(2)
        except NoSuchElementException:
            print("O Usuário não possui foto(s) ou você não tem permissão.") 

    def next_pic(self):    
        button_next = "//a[text()=\"Próximo\"]"        
        try:
            self.driver.find_element_by_xpath(button_next).click()
            time.sleep(3)
            return True
        except NoSuchElementException:
            try:
                self.like()
            except:
                pass
            print("- Usuário não possui mais fotos seguintes.")
            return False

    def like_unstoppable(self):        
        # Curte fotos até o final do perfil ou interrupção
        
        self.open_1st_pic()
        self.like()
        while(True):
            hasProxPost = self.next_pic()
    
            # Se tiver botão de próxima foto -> esperado TRUE
            if hasProxPost == True:
    
                # Curtir
                self.like()
                time.sleep(2)

                # Botão próximo
                self.next_pic()
                time.sleep(2)    
            
            # Se não tiver botão de próxima foto    
            else:
                print("- Não há mais fotos disponíveis para serem curtidas.")
                break

    def like(self):
        button_like = self.driver.find_element_by_class_name('fr66n')
        soup = bs(button_like.get_attribute('innerHTML'),'html.parser')
        
        if(soup.find('svg')['aria-label'] == 'Curtir'):
            button_like.click()
        time.sleep(2)

    def like_photo_by_quantity(self):
        quantity = int(input("Quantas fotos deseja curtir? "))
        
        self.open_1st_pic()
        self.like()
        i = 1
        while(i < quantity):
            self.next_pic()
            self.like()
            i+=1
        
    def follow(self):
        try:            
            self.driver.find_element_by_xpath('//button[text()="Seguir"]').click()
        except:
            pass    
     
    def open_direct(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'xWeGp'))).click()
        except:
            pass
        
    def send_message(self):
        self.open_direct()
        
        messageforwho = input("Enviar mensagem para: ")
        message = input("Mensagem: ")
    
        try:
            WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Enviar mensagem"]'))).click()                                    
        except:
            pass
        
        self.driver.find_element_by_xpath('//input[@name="queryBox"]').send_keys(messageforwho)
        time.sleep(4)
        
        # Selecionar o radio do destinatario
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".dCJp8:nth-of-type(1)"))).click()
        
        # Botão de confirmar destinatario
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "rIacr"))).click()
        
        # Enviar mensagem ao textarea
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))).send_keys(message) 
        
        # Botão enviar mensagem
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Enviar"]'))).click()   
    
    def close_window(self):
        print("Fechando webdriver...")
        time.sleep(4)
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()
