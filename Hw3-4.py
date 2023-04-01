#Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

#Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

#Test Caseler;

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


#?class adları by ile yazılan 

class Test_Sauce:

# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
# "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
   
    def test_invalid_login(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("ecret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"Result of Test: {testResult}")
        sleep(3)

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_empty_bothOfThem(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)

        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username is required"
        print(f"Result of Test: {testResult}")

#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak 
# "Epic sadface: Password is required" gösterilmelidir.
    def test_empty_password(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)

        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("user name")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"Result of Test: {testResult}")

#Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
#  Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
#  (Tek test casede işleyiniz)

    def test_icon(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        

        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        x=driver.find_elements(By.CLASS_NAME,"error_icon")
        sleep(2)
        xNum=len(x)
       

        if xNum==2:
            testResult=True
            print(f"Result of Test: {testResult}")
            sleep(3)
            loginBtn=driver.find_element(By.CLASS_NAME,"error-button")
            loginBtn.click()
            sleep(3)
            y=driver.find_elements(By.CLASS_NAME,"error-button")
            sleep(2)
            yNum=len(y)


            if yNum==0:
                 print(f"Result of Test: {testResult}") 
                 sleep(2)

            else:
                testResult=False
                print(f"Result of Test: {testResult}")
                sleep(2)
        else:
            testResult=False
            print(f"Result of Test: {testResult}")
            sleep(3)

       
 #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.       
    def standard_user(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(5)


#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır
    def products(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)

        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)

        listOfProducts=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Number of Products: {len(listOfProducts)}")
        sleep(2)





testClass = Test_Sauce()

testClass.test_invalid_login()
testClass.test_empty_bothOfThem()
testClass.test_empty_password()
testClass.test_icon()
testClass.products()
testClass.standard_user()
