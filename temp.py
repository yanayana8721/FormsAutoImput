import random

from selenium import webdriver
from time import sleep

sleep(random.uniform(20,540))

url = ''
password = ''
email = ''

browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_id('i0116').send_keys(email)
browser.find_element_by_id('idSIButton9').click()
sleep(3)

browser.find_element_by_id('i0118').send_keys(password)
browser.find_element_by_id('idSIButton9').click()
sleep(3)
browser.find_element_by_id('idSIButton9').click()
sleep(3)

browser.find_element_by_xpath("//imput[@value='ない']")[0].click()
sleep(3)

browser.find_element_by_xpath("//button[@title='送信']").click()
sleep(20)

browser.quit()


