class CreditCard:
    def __init__(self,driver):
        self.driver = driver
        self.config = self.driver.config

    def setCreditcard(self):
        #等待信用卡頁面出現
        self.driver.waitUntilAppear("// input[@id = 'CardNumber']")
        #選擇信用卡種類 0:Visa 1:MasterCard 2:JCB
        self.driver.selectValue('CardType', self.config['CREDITCARD']['cardType'])
        #輸入信用卡卡號
        self.driver.inputID('CardNumber',self.config['CREDITCARD']['taishin-account'])
        #輸入有效月份
        self.driver.selectValue('ExpireMonth', self.config['CREDITCARD']['taishin-year'])
        #輸入有效年份
        self.driver.selectValue('ExpireYear', self.config['CREDITCARD']['taishin-month'])
        #輸入CVN
        self.driver.inputID('CVN', self.config['CREDITCARD']['CVN'])
        #輸入購買人姓氏
        self.driver.inputID('FirstName', self.config['CREDITCARD']['firstName'])
        #輸入購買人名字
        self.driver.inputID('LastName', self.config['CREDITCARD']['lastName'])
        #獲取OTP
        self.driver.clickItem("//input[@id = 'otpajax']")

        #輸入OTP密碼
        OTP_name = input('')
        if OTP_name != '':
            self.driver.inputID('OTP',OTP_name)
            self.driver.clickButton("//button[@class ='btn']")
