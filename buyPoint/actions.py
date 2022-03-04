import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os.path import dirname, join, abspath
import configparser     # for using .ini file
import platform
# for clearInput()
from selenium.webdriver.chrome.options import Options
# for monitoring http request/response

class Actions:
    def __init__(self,environment):

        # options = webdriver.ChromeOptions()
        # 1. enable to capture network logs
        # options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
        # caps = DesiredCapabilities.CHROME
        # caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        # 啟用 Chrome browser

        #設定chromedriver 路徑 此範例for mac
        webdriver_chrome_path = '/usr/local/bin/chromedriver'
        options = Options()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(webdriver_chrome_path)
        # self.driver = webdriver.Chrome(options=options)


        # 開啟設定檔 account.ini
        ini_file_name = "account.ini"
        self.config = self.getConfig(ini_file_name)

        # 前往 Gash 網站
        self.gotoURL(self.config['WEBSITES'][environment])


    def getConfig(self, ini_file_name):
        configuration = configparser.ConfigParser()
        configuration.optionxform = str
        configuration.read(ini_file_name)
        return configuration

    def gotoURLDirect(self, URL):
        self.driver.get(URL)

    # 前往頁面 environment = 'gashxxx', ''
    def gotoURL(self, environment):
        environment = self.config['WEBSITES']['environment']
        website = self.config['WEBSITES'][environment]
        self.driver.get(website)

    # 移動游標
    def moveTo(self, xpath):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath)))).perform()

    # 移動游標並點擊 Item
    def clickItem(self, xpath):
        # 等待 xpath 出現（這裡假設 xpath 正確）
        WebDriverWait(self.driver, 300).until(lambda driver: driver.find_element_by_xpath(xpath))
        element = self.driver.find_element_by_xpath(xpath)
        #         self.driver.execute_script("arguments[0].click();", element)
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))).perform()
        ActionChains(self.driver).click().perform()
        sleep(1)

    #點選所有checkbox
    def clickCheckbox(self,name):
        checkboxs = self.driver.find_elements_by_class_name(name)
        for checkbox in checkboxs:
            checkbox.click()
            time.sleep(0.3)

    #輸入欲選擇下拉式選單的值
    def selectValue(self, id, value):
        select = Select(self.driver.find_element_by_id(id))
        select.select_by_value(value)

    # 輸入欲選擇下拉式選單的index
    def selectIndex(self,id,index):
        select = Select(self.driver.find_element_by_id(id))
        select.select_by_index(index)

    # 雙點擊 Item
    def doubleClickItem(self, xpath):
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(xpath)).perform()
        sleep(1)

    # 點擊按鈕
    def clickButton(self, xpath):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))).click()
        # sleep(1)

    #設定重整頁面
    def refresh(self):
        self.driver.refresh()

    #想要定位其中的iframe並切進去
    def switchFrame(self,frame):
        self.driver.switch_to.frame(frame)

    #找class name並submit
    def findClass(self,class_name):
        self.driver.find_element_by_class_name(class_name).submit()

    # 上一頁
    def goBack(self):
        self.driver.back()

    # 定位xpath輸入content
    def inputXpath(self, xpath, content):
        self.driver.find_element_by_xpath(xpath).send_keys(content)

    # 定位id 輸入content
    def inputID(self, id, content):
        self.driver.find_element_by_id(id).send_keys(content)

    # 定位name 輸入content
    def inputName(self, name, content):
        self.driver.find_element_by_id(name).send_keys(content)

    #清除input
    def clearInput(self, xpath):
        sleep(0.1)
        # 取得 input 當前內容，若有 value 則清空
        while self.getAttribute(xpath, "value") != "":
            if (platform.system() == "Darwin"):  # mac
                self.driver.find_element_by_xpath(xpath).send_keys(Keys.COMMAND, "a")
            else:
                self.driver.find_element_by_xpath(xpath).send_keys(Keys.CONTROL, "a")
            sleep(0.2)
            self.driver.find_element_by_xpath(xpath).send_keys(Keys.BACK_SPACE)
        sleep(1)

    # 等待按鈕可以按
    def waitUntilButtonEnable(self, xpath):
        WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))

    # 等待 Item 出現
    def waitUntilAppear(self, xpath):
        WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

    # 等待 Item 消失
    def waitUntilDisappear(self, xpath):
        WebDriverWait(self.driver, 300).until(
            EC.invisibility_of_element_located((By.XPATH, xpath)))

    # 判斷是否存在
    def isExist(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            '''
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            '''
            return True
        except:
            return False
        # 等待 Item 出現，並判斷是否存在

    def isExistAfterAppear(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

"""
 # 獲得當下視窗控制代碼
    def getWindowHandles(self, index):
        return self.driver.window_handles[index]

    # 切換視窗
    def switchtoWindow(self, handle):
        self.driver.switch_to_window(handle)

    # 關掉跳出的提示訊息
    def closeMessages(self):
        while self.isExist("//i[@class='el-message__closeBtn el-icon-close']"):
            self.clickItem("//i[@class='el-message__closeBtn el-icon-close']")
    def isSelected(self, xpath):
        return self.driver.find_element_by_xpath(xpath).is_selected()

    # 關閉分頁
    def closeTab(self, handle):
        if handle != self.driver.current_window_handle:
            self.switchtoWindow(handle)
        self.driver.close()

    # 取得符合資格的元素 list
    def getElements(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)
    def getHttpResponses(self, request_id):
        return self.driver.execute_cdp_cmd('Network.getResponseBody',{'requestId': request_id})

    # 取得所有符合 method 和 url 的 xhr responses
    def getResponsesJson(self, method, url):
        '''
            inputs:
                method = "Network.responseReceived"
                url = "https://public." + self.config['WEBSITES']['environment'] + ".sis.ai/ask/componentData"
            outputs:
                a list of responses in json format
            usage:
                responses_json = self.driver.getResponsesJson(method, url)
        '''
        # 取得 logs
        logs = self.getHttpRequests()
        responses_json = []
        # 篩選 log
        for log in logs:
            request_json = json.loads(log['message'])
            # 將 request_json 中符合 method = 'Network.responseReceived'
            # 以及 params type = 'xhr'
            # 以及 params response url 符合 input url 的 request_id 取出
            if (request_json['message']['method'] == method
               # 確認 http request url = https://public.qa.sis.ai/ask/componentData
               and request_json['message']['params']['response']['url'] == url
               # 確認 http request type = XHR(XmlHttpRequest)，而非 type = preflight
               and request_json['message']['params']['type'] == 'XHR'):
                request_id = request_json['message']['params']['requestId']
                # 以符合條件的 request_id，取得 response
                try:
                    response = self.getHttpResponses(request_id)
                    response_json = json.loads(response['body'])
                    responses_json.append(response_json)
                except Exception as e:  # 略過沒有 response_body 的 request
                    msg = "just for skip, do NOT show"
                    #print("error")
        return responses_json
        # 取得元件的文字敘述
    def getText(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text

    # 取得 class_name 的 attribute
    def getAttribute(self, xpath, class_name):
        element = self.driver.find_element_by_xpath(xpath)
        return element.get_attribute(class_name)

"""
"""      
    def getHttpRequests(self):
        '''
        :Usage:
            # 清空 http requests
            self.driver.getHttpRequests()
            # 獲取上一次 getHttpRequests() 之後到這一次 getHttpRequests() 之間的 http requests
            logs = self.driver.getHttpRequests()
        '''
        return self.driver.get_log("performance")    
    def getHttpResponses(self, request_id):
        return self.driver.execute_cdp_cmd('Network.getResponseBody',{'requestId': request_id})
  
    def getResponsesJson(self, method, url):
        '''
            inputs:
                method = "Network.responseReceived"
                url = "https://public." + self.config['WEBSITES']['environment'] + ".sis.ai/ask/componentData"
            outputs:
                a list of responses in json format
            usage:
                responses_json = self.driver.getResponsesJson(method, url)
        '''
        # 取得 logs
        logs = self.getHttpRequests()
        responses_json = []
        # 篩選 log
        for log in logs:
            request_json = json.loads(log['message'])
            # 將 request_json 中符合 method = 'Network.responseReceived'
            # 以及 params type = 'xhr'
            # 以及 params response url 符合 input url 的 request_id 取出
            if (request_json['message']['method'] == method
               # 確認 http request url = https://public.qa.sis.ai/ask/componentData
               and request_json['message']['params']['response']['url'] == url
               # 確認 http request type = XHR(XmlHttpRequest)，而非 type = preflight
               and request_json['message']['params']['type'] == 'XHR'):
                request_id = request_json['message']['params']['requestId']
                # 以符合條件的 request_id，取得 response
                try:
                    response = self.getHttpResponses(request_id)
                    response_json = json.loads(response['body'])
                    responses_json.append(response_json)
                except Exception as e:  # 略過沒有 response_body 的 request
                    msg = "just for skip, do NOT show"
                    #print("error")
        return responses_json

"""
