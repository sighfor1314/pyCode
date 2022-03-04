class BuyGash:
    def __init__(self,driver):
        self.driver = driver
        self.config = self.driver.config

    def buyGash(self):
        #等待欄位出現
        self.driver.waitUntilAppear("//input[@id='mobileNumber']")
        #輸入電話號碼
        self.driver.inputID("mobileNumber",self.config['ACCOUNT-INFO']['phone_number'])
        #輸入email
        self.driver.inputID('email',self.config['ACCOUNT-INFO']['email'])
        #選則付款方式 0:橘子支付 1:WebATM 2:信用卡支付
        self.driver.selectIndex('paid',self.config['ACCOUNT-INFO']['paid_method'])
        #輸入coupon
        self.driver.inputID('CouponPin', self.config['ACCOUNT-INFO']['coupon'])
        #勾選同意條款checkbox
        self.driver.clickCheckbox('label-btn')
        #點選我要購買
        self.driver.clickItem("//a[contains(text(),'我要購買')]")
        #點選進行結帳
        self.driver.clickItem("//a[contains(text(),'進行結帳')]")


