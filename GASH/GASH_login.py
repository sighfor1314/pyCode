
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def Login():

    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome('chromedriver', chrome_options=options)
    chrome.get("http://tw.gashpoint.com/")
    chrome.find_element_by_class_name("link-trans").click()
    #chrome.get("https://reurl.cc/dx27Wk")


""""
email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('doris.yin@kyperdata.com')
password.send_keys('d08130918')
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
soup = BeautifulSoup(chrome.page_source, 'html.parser')
titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ojkyduve'})

for title in titles:

    post = title.find('span', {'dir': 'auto'})

    if post:
        print(post.getText())

chrome.quit()
"""