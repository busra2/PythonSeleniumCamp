from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://www.google.com.tr/?client=safari")

input =driver.find_element(By.NAME,"q")
print(f"ınput:{input}")#buldu o yüzden nesne var uyrısı döner 
input.send_keys("kodlamaio")

serachButton=driver.find_element(By.NAME,"btnK")
sleep(2)
serachButton.click()

#kodlamaio sitesini seçip tıklamak
firstResult=driver.find_element(By.XPATH,"")






while True:
    continue 