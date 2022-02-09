
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from GASH_payment import Payment
import time

class BuyGash:
    def buyGash(self):
    # login()
        options = Options()
        options.add_argument("--disable-notifications")
        chrome = webdriver.Chrome('chromedriver', chrome_options=options)
        chrome.get("https://reurl.cc/dx27Wk")
        phone_number = chrome.find_element_by_id("mobileNumber")
        email = chrome.find_element_by_id('email')
        paid = Select(chrome.find_element_by_id('paid'))
        couponPin = chrome.find_element_by_id('CouponPin')


        phone_number.send_keys('0958983333')
        email.send_keys('sighfor1314@gmail.com')
        paid.select_by_index(2)

        couponNumber = ''
        if couponNumber != '':
            couponPin.send_keys(couponNumber)

        #print(len(chrome.find_elements_by_css_selector('input[type = checkbox]')))
        checkboxs = chrome.find_elements_by_class_name('label-btn')
        for checkbox in checkboxs:
            checkbox.click()
            time.sleep(0.5)

        chrome.find_element_by_id('checkout').click()
        chrome.find_element_by_id('btnPay').click()

        Payment(chrome)
        time.sleep(60)

