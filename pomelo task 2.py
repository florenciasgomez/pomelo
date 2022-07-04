#enviroment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

#paraeldriveChorme
driver = webdriver.Chrome (executable_path=r"C:\dchrome\chromedriver.exe")
driver.get ("https://www.google.com/")
driver.maximize_window()

#searchpomeloenboxsearch
search= driver.find_element(by=By.NAME, value="q")
search.send_keys("pomelo")
time.sleep(1)

options = driver.find_elements (By.XPATH, "//li[@class='sbct']//b")  

for i in range(len(options)):
    element = options[0]
    text = element.text 
    if text == "fintech":   
        assert text == "fintech"
        element.click() 
        time.sleep(1)

pomelo = driver.find_elements(By.XPATH, "//div[@id='search']//h3")[0].click()
time.sleep(1) 
assert "pomelo" in driver.title
driver.quit()

