

import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="/Users/synergies/Downloads/instantclient_19_8")
# import csv

# path = 'data003.csv'
# with open(path, newline='') as csvfile:
#     rows = csv.reader(csvfile, delimiter=',')
#     headers = next(rows)
#     print('headers: %s' % headers)

#　－－－－－連線資料庫－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 連線方法　使用者名稱/密碼/ 地址和埠號

conn = cx_Oracle.connect("system", "oracle", "192.168.66.107:1522/xe")
cur = conn.cursor()

cur.execute("CREATE TABLE oracle流程 ( id int,c_char VARCHAR(255), c_char1 VARCHAR(255),n_int int,b_boolean int,t_time VARCHAR(255))")


conn.commit()

cur.close()