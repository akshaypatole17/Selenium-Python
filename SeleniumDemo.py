'''
Created on 14-Oct-2018

@author: Akshay
'''

print("Hello Akshay, Lets login to your facebook account")

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

url = "https://www.facebook.com"
driver = webdriver.Firefox(executable_path='F:\Akshay Study\Study IT\Selenium\Project Files\Geckodriver\geckodriver-v0.21.0-win64\geckodriver.exe')

driver.get(url)

username = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')
submit = driver.find_element_by_id("u_0_2")

username.send_keys("akshaypatole17@gmail.com")
password.send_keys("Password")

submit.click()

driver.quit()