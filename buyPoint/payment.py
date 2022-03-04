class Payment:
    def __init__(self,driver):
        self.driver = driver
        self.config = self.driver.config

    def payment(self):
        # 等待欄位出現
        self.driver.waitUntilAppear("// input[@id = 'MobileNumber']")
        #選擇統一發票 0:我要捐贈 1:個人電子發票 2:三聯式發票
        self.driver.selectIndex('InvoiceType', self.config['ACCOUNT-INFO']['invoiceType'])
        #輸入公司抬頭或姓名
        self.driver.inputID('CompanyName',self.config['ACCOUNT-INFO']['purchaser'])
        #選擇電子發票載具類別 0:未持有 1:手機條碼 2:自然人憑證條碼
        self.driver.selectIndex('CarrierType', self.config['ACCOUNT-INFO']['carrierType'])
        #輸入載具
        self.driver.inputID('MobileId', self.config['ACCOUNT-INFO']['barcode'])
        #點選確認
        self.driver.clickItem("//input[@id ='inv_btn']")


