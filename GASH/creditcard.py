from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from GASH_login import Login
from selenium.webdriver.support.ui import Select
from Bank_OTP import *




def CreditCard(chrome):
    chrome.implicitly_wait(30)
    cardType = Select(chrome.find_element_by_id('CardType'))
    cardNumber = chrome.find_element_by_id('CardNumber')
    expireMonth = Select(chrome.find_element_by_id('ExpireMonth'))
    expireYear = Select(chrome.find_element_by_id('ExpireYear'))
    CVN = chrome.find_element_by_id('CVN')
    firstName = chrome.find_element_by_id('FirstName')
    lastName = chrome.find_element_by_id('LastName')
    otpajax = chrome.find_element_by_id('otpajax')
    OTP = chrome.find_element_by_id('OTP')

    cardType.select_by_value('//')
    cardNumber.send_keys('//')
    expireMonth.select_by_value('//')
    expireYear.select_by_value('//')
    CVN.send_keys('//')
    firstName.send_keys('//')
    lastName.send_keys('//')
    otpajax.click()
    OTP_name = input('')
    if OTP_name != '':
        OTP.send_keys(OTP_name)
        time.sleep(1)
        chrome.find_element_by_class_name('btn').submit()


    taishinbank_OTP(chrome)
    # time.sleep(300)