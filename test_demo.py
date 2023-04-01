from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date



class Test_DemoClass:
    #her testten önce çağırılır
    def setup_method(self):
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
       
        
        
    #her testten sonra çağırılır
    def teardown_method(self):
        self.driver.quit()

    
    @pytest.mark.parametrize("username,password",[("1","1") , ("kullaniciadım","sifrem")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
  # Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.      
    def test_empty_bothOfThem(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-Empty-Both-Of-Them.png")
        assert errorMessage.text=="Epic sadface: Username is required"
        
#Sadece şifre alanı boş geçildiğinde
    @pytest.mark.parametrize("username,password",[("ad1",""),("ad2",""),("ad3","")] )
    def test_empty_password(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-Empty-Password.png")
        assert errorMessage.text=="Epic sadface: Password is required"
        
#Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
#Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
    def test_icon(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        x = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.waitForElementVisible((By.CLASS_NAME,"error_icon"))
        xNum=len(x)
        self.driver.save_screenshot(f"{self.folderPath}/test-x-icon.png")
        
        if xNum==2:
            loginBtn=self.driver.find_element(By.CLASS_NAME,"error-button")
            y=self.driver.find_elements(By.CLASS_NAME,"error-button")
            loginBtn.click()
            yNum=len(y)
            #self.waitForElementVisible((By.CLASS_NAME,"error-button"))
            self.driver.save_screenshot(f"{self.folderPath}/test-icon-numbers.png")
            assert True
            
        else:
            assert False
            
#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.  
    def test_standard_user(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        pageMsg = self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-standart-user.png")
        assert pageMsg == "https://www.saucedemo.com/inventory.html"
        
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır      
    def test_products(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        listOfProducts=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.save_screenshot(f"{self.folderPath}/number-of-products-{len(listOfProducts)}.png")
        assert True
    
  
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))