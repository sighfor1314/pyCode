import smtplib
from email.mime.text import MIMEText

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:

        mime = MIMEText("你好世界 hollo world!", "plain", "utf-8")  # 撰寫內文內容，以及指定格式為plain，語言為中文
        mime["Subject"] = "test測試"  # 撰寫郵件標題
        mime["From"] = "sighfor1314@gmail.com"  # 撰寫你的暱稱或是信箱
        mime["To"] = "sighfor1314@gmail.com"  # 撰寫你要寄的人
        # mime["Cc"] = "@gmail.com, @gmail.com"  # 副本收件人
        # msg = mime.as_string()  # 將msg將text轉成str
        # msg = 'Subject: testing \n\
        #             From:abc \n\
        #             To:sighfor1314@gmail.com\n\
        #             testinggggggg'
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("sighfor1314@gmail.com", "cludpwyjuubaaukt")  # 登入寄件者gmail

        smtp.send_message(mime)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)

