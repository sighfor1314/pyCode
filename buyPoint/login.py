# from actions import Actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Login:
    def __init__(self,driver):
        self.driver = driver
        self.config = self.driver.config

    def login(self):

        # chrome.get("http://tw.gashpoint.com/")
        # chrome.find_element_by_class_name("link-trans").click()
        #chrome.get("https://reurl.cc/dx27Wk")


