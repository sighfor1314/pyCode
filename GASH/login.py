
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def Login():

    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome('chromedriver', chrome_options=options)
    chrome.get("http://tw.gashpoint.com/")
    chrome.find_element_by_class_name("link-trans").click()
    #chrome.get("https://reurl.cc/dx27Wk")


