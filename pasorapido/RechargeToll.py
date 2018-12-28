import logging
import logging.config
import os, pdb
import time

from selenium import webdriver

#logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
#logger = logging.getLogger(__name__)

url = "https://pasorapido.gob.do/Account/Login?ReturnUrl=%2Fmicuenta%2Forden"
user = os.getenv('USERNAME')
pwd = os.getenv('PASSWORD')


def recharge_toll(user_id, pwd):

   # try:

    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    user_name = driver.find_element_by_id("UserName")
    user_name.send_keys(user)

    password = driver.find_element_by_name('Password')
    password.send_keys(pwd)

    login = driver.find_element_by_class_name('entrar')
    login.submit()
   # pdb.set_trace()
    # recharge = driver.find_element_by_class_name('pull-right')
    # recharge.submit()
    btns = driver.find_elements_by_xpath("//button[@class='btn btn-warning pull-right'][1]")
    for btn in btns:
        print("Hello" + btn)
    # driver.find_element_by_tag_name('button').click()
    # recharge.submit()
    # btn btn-warning pull-right
    # assert "No results found." not in driver.page_source
    #time.sleep(5)
    # driver.quit()
    # btn btn-warning pull-right
   # except Exception as e:
    # driver.quit()
  #      logger.error(e)


recharge_toll(user, pwd)
