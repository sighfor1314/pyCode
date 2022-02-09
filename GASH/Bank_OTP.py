from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from GASH_login import Login
from selenium.webdriver.support.ui import Select
import time


def taishinbank_OTP(chrome):

    chrome.implicitly_wait(35)
    chrome.refresh()
    chrome.implicitly_wait(35)
    chrome.switch_to.frame('challengeMethodIframe')
    chrome.find_element_by_class_name('btn.btn-block.btn-primary.mb-1').submit()
    chrome.implicitly_wait(35)
    code = chrome.find_element_by_id('code')
    OTP_name = input('bankOTP')
    if OTP_name != '':
        code.send_keys(OTP_name)
        time.sleep(1)
        chrome.find_element_by_class_name('btn.btn-block.btn-primary.mb-1').submit()

#def cathaybank_OTP(chrome):



