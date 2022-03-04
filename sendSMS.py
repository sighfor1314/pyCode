from twilio.rest import Client
import random
import string
account_sid = 'ACda5033c7eadd21c8a6975705fe8936f8'
auth_token = '9999bbf75e01505837c18bff3888602f'
client = Client(account_sid, auth_token)
key = ''.join(random.sample(string.digits, 6)) #你要傳送的驗證碼(這裡我用的隨機數字)
message = client.messages.create(
 from_='+12207664744',
 body=key,
 to='+886962037850'
 )
n=input("輸入驗證碼")
if n==key:
 print('驗證成功')
else:
 print('驗證失敗')


