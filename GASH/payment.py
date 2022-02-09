from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from GASH_login import Login
from selenium.webdriver.support.ui import Select
from CreditCard_payment import CreditCard


def Payment(chrome):
    chrome.implicitly_wait(30)
    invoiceType = Select(chrome.find_element_by_id('InvoiceType'))
    companyName = chrome.find_element_by_id('CompanyName')
    carrierType = Select(chrome.find_element_by_id('CarrierType'))
    mobileId = chrome.find_element_by_id('MobileId')

    invoiceType.select_by_index(1)
    companyName.send_keys('尹佳玲')
    carrierType.select_by_index(1)
    mobileId.send_keys('/4VMQY9R')

    chrome.find_element_by_id('inv_btn').click()
    CreditCard(chrome)
