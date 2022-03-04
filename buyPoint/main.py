from buy_gash import BuyGash
from actions import Actions
from payment import Payment
from creditcard import CreditCard
from setOTP import SetOTP
def main():
   environment = "gash5400"
   driver = Actions(environment)
   gash =BuyGash(driver)
   gash.buyGash()
   gash = Payment(driver)
   gash.payment()
   gash =CreditCard(driver)
   gash.setCreditcard()
   gash = SetOTP(driver)
   gash.taishinBank()

if __name__ == '__main__':
   main()