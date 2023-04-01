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
        self.waitForElementVisible((By.ID,"user-name"),5)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text=="Epic sadface: Username and password do not match any user in this service"

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))