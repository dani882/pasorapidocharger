import os
import time

from selenium import webdriver

url = "https://pasorapido.gob.do/Account/Login?ReturnUrl=%2Fmicuenta%2Forden"

user = os.getenv('USERNAME')
pwd = os.getenv('PASSWORD')

driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)

user_name = driver.find_element_by_name('UserName')
user_name.send_keys(user)

password = driver.find_element_by_name('Password')
password.send_keys(pwd)

login = driver.find_element_by_class_name('entrar')
login.submit()
