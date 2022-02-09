
import csv
import pandas as pd
import mysql.connector


#　－－－－－連線資料庫－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 連線方法　使用者名稱/密碼/ 地址和埠號

# mysql 要  %s





mydb = mysql.connector.connect(

  host="dbs.dev.sis.ai",
  user="root",
  password="jarvix123",
  database="Doris_test"

)

mycursor = mydb.cursor()
def setSqlInsertion(path,table_name):
    try:
        with open(path, newline='') as csvfile:

            data = pd.read_csv(path)

            column_lengh = len(data.values[0])
            column_count = ""
            for i in range(1, column_lengh + 1):
                column_count += '%s'
                if i != column_lengh:
                    column_count += ','
            print(column_count)
            rows = [tuple(x) for x in data.values]
            print(rows)
            sql_insert = "INSERT INTO %s VALUES (%s)" % (table_name, column_count)

            print(sql_insert)
            mycursor.executemany(sql_insert, rows)
            mydb.commit()
    except Exception as e:
        print(e)
    # finally:
    #     print ('insert function done')

table_name='qaTest1'
path = 'data003.csv'
setSqlInsertion(path,table_name)

mycursor.close()