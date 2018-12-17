import time
from selenium import webdriver

url = "https://pasorapido.gob.do/Account/Login?ReturnUrl=%2Fmicuenta%2Forden"

driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)

user_name = driver.find_element_by_name('UserName')
user_name.send_keys("dani882")

password = driver.find_element_by_name('Password')
password.send_keys("jesusrivera")

login = driver.find_element_by_class_name('entrar')
login.submit()
