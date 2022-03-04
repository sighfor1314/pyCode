class SetOTP:
    def __init__(self,driver):
        self.driver = driver
        self.config = self.driver.config

    def taishinBank(self):
        #等待台新銀行付款頁出現
        self.driver.waitUntilAppear("//*[@name = 'challengeMethodIframe']")
        #要執行此才可以順利找到元件 重要！！！！
        self.driver.switchFrame('challengeMethodIframe')
        #取得otp密碼
        self.driver.findClass('btn.btn-block.btn-primary.mb-1')

        #輸入銀行端OTP
        OTP_name = input('bankOTP')
        if OTP_name != '':
            #從手機取得透過cmd輸入OTP密碼
            self.driver.inputID('code', OTP_name)
            #確認購買
            self.driver.findClass('btn.btn-block.btn-primary.mb-1')





