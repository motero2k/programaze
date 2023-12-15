# Generated by Selenium IDE
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

# Usage save_page_html(self.driver), save the page in page.html (userful for debugging)
def save_page_html(driver):
      try:
          with open("page.html", "w", encoding="utf-8") as file:
              file.write(driver.page_source)
          print("HTML guardado correctamente en 'page.html'.")
      except Exception as e:
          print(f"Error al guardar el HTML: {e}")

#--------------------------TESTS---------------------------------
# use above a function:   @pytest.mark.skip(reason="no way of currently testing this") to skip a test
# print(self.driver.current_url) to print the current url
class Test_selenium():
    
    
    def setup_method(self, method):
      #user Options instead of DesiredCapabilities
      options = webdriver.ChromeOptions()
      options.add_argument('--no-sandbox')
      options.add_argument('--disable-dev-shm-usage') 
      self.driver = webdriver.Remote(command_executor='http://host.docker.internal:4444/wd/hub', options=options)
      self.driver.set_page_load_timeout(30)
      self.driver.implicitly_wait(5)


    def teardown_method(self, method):
      self.driver.quit()

    def test_login(self):
      URL = "http://host.docker.internal/login"
      self.driver.get(url=URL)
      
      self.driver.find_element(By.ID, "email").send_keys("test")
      self.driver.find_element(By.ID, "password").send_keys("test")
      self.driver.find_element(By.ID, "submit").click()
      #print(self.driver.current_url)
      #if login is successful, the user is redirected to the innsoft_days page
      assert self.driver.current_url == "http://host.docker.internal/innsoft_days"
      

    def test_failed_login(self):
      URL = "http://host.docker.internal/login"
      self.driver.get(url=URL)
      self.driver.find_element(By.ID, "email").send_keys("test@test.com")
      self.driver.find_element(By.ID, "password").send_keys("wrong password")
      self.driver.find_element(By.ID, "submit").click()
      #print(self.driver.current_url)
      #if login is unsuccessful, the user is redirected to the login page``
      assert self.driver.current_url == "http://host.docker.internal/login"

    
    def test_create_proposal(self):
      self.test_login() #login first <-------------------------- REALLY IMPORTANT
      
      self.driver.find_element(By.LINK_TEXT, "Acciones").click()
      self.driver.find_element(By.LINK_TEXT, "Listar propuestas").click()
      #in chrome, developer tools, elements, right click on the element and copy xpath
      tokens_web_element = self.driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div/b/span')[0]
      tokens_count = int(tokens_web_element.text)
      self.driver.find_element(By.LINK_TEXT, "CREAR PROPUESTA").click()
      self.driver.find_element(By.ID, "subject").send_keys("Una propuesta divertida")
      self.driver.find_element(By.ID, "description").send_keys("Descripccion")
      dropdown = self.driver.find_element(By.ID, "proposal_type")
      dropdown.find_element(By.XPATH, "//option[. = 'ACTIVIDAD']").click()
      self.driver.find_element(By.ID, "submit").click()
      tokens_web_element2 = self.driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div/b/span')[0]
      tokens_count2 = int(tokens_web_element2.text)
      print("\nTokens before: " + str(tokens_count) + ". Tokens after proposal: " + str(tokens_count2))
      assert tokens_count2 == tokens_count - 1
        

  
