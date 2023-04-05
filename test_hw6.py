from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import openpyxl
from constants import globalConstants 


class Test_ClassHw6:
    
     def setup_method(self):
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.driver.get(globalConstants .URL)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
     def teardown_method(self):
         self.driver.quit()
         
         
     def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
         
         #sepete ürün eklendi mi ?
     def test_add_shopping(self):
         self.waitForElementVisible((By.ID,"user-name"))
         usernameInput = self.driver.find_element(By.ID, "user-name")
         self.waitForElementVisible((By.ID,"password"))
         passwordInput = self.driver.find_element(By.ID,"password")
         
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         
         loginBtn=self.driver.find_element(By.ID,"login-button")
         loginBtn.click()
         
         self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-backpack"))
         removeBtn1 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
         removeBtn1.click()
         self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-bike-light"))
         removeBtn2 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
         removeBtn2.click()
         
         
         self.driver.save_screenshot(f"{self.folderPath}/test-add-shopping.png")
         assert True
         
    #
     @pytest.mark.parametrize("count_cart",[(1),(2),(3),(4)])
     def test_add_to_cart_process(self,count_cart):
         self.waitForElementVisible((By.ID,"user-name"))
        
         usernameInput = self.driver.find_element(By.ID, "user-name")
         passwordInput = self.driver.find_element(By.ID,"password")
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         loginBtn = self.driver.find_element(By.ID,"login-button")
         loginBtn.click()
        
         self.waitForElementVisible((By.CLASS_NAME,"btn_inventory"))
         add_and_remove_card_btns=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")

         for index in range(count_cart):
             if(add_and_remove_card_btns[index].text=="Add to cart"):
               add_and_remove_card_btns[index].click()            

         assert self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text==str(count_cart)
         
     @pytest.mark.parametrize("first_name,surname,postalCode",[("busra","seher","1234")])    
     def test_swag_lags(self,first_name,surname,postalCode):
         self.waitForElementVisible((By.ID,"user-name"))
         usernameInput = self.driver.find_element(By.ID, "user-name")
         self.waitForElementVisible((By.ID,"password"),10)
         passwordInput = self.driver.find_element(By.ID,"password")
         
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         
         loginBtn=self.driver.find_element(By.ID,"login-button")
         loginBtn.click()
         
         loginBtn2 =self.driver.find_element(BY.XPATH,"//*[@id=shopping_cart_container]/a")
         loginBtn2.click()
         site1=self.driver.current_url
         
         if  site1==self.driver.current_url:
             self.waitForElementVisible((BY.XPATH,"//*[@id=checkout]"),15)
             loginBtn3 =self.driver.find_element(BY.XPATH, "//*[@id=checkout]")
             loginBtn3.click()
             self.waitForElementVisible((By.ID,"first-name"))
             usernameInput = self.driver.find_element(By.ID, "first-name")
             self.waitForElementVisible((By.ID,"last-name"),10)
             lastName = self.driver.find_element(By.ID,"last-name")
             self.waitForElementVisible((By.ID,"postal-code"),10)
             codeInput = self.driver.find_element(By.ID, "postal-code")
             usernameInput.send_keys(first_name)
             lastName.send_keys(surname)
             codeInput.send_keys(postalCode)
             loginBtn4 = self.driver.find_element(By.ID,"continue")
             loginBtn4.click()
             self.driver.save_screenshot(f"{self.folderPath}/test-swag-lags.png")
             assert True
              
         else:
             assert False 
         
         

         
        
         
         
       
         
         
     def test_logout(self):
         self.waitForElementVisible((By.ID,"user-name"))
         usernameInput = self.driver.find_element(By.ID, "user-name")
         self.waitForElementVisible((By.ID,"password"),10)
         passwordInput = self.driver.find_element(By.ID,"password")
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         loginBtn = self.driver.find_element(By.ID,"login-button")
         loginBtn.click()

         self.waitForElementVisible((By.ID,"react-burger-menu-btn"),10)
         menu = self.driver.find_element(By.ID,"react-burger-menu-btn")

         menu.click()
         self.waitForElementVisible((By.ID,"logout_sidebar_link"),10)
         logoutBtn = self.driver.find_element(By.ID,"logout_sidebar_link")

         logoutBtn.click()
         WebDriverWait(self.driver,5).until(ec.url_to_be(globalConstants.URL))

         print(self.driver.current_url)

         self.driver.save_screenshot(f"{self.folderPath}/test_logout.png")
         assert ec.url_to_be(globalConstants.URL)
         
        

        
        
        
       
    
    