
import csv
import pandas as pd
import pymssql


#　－－－－－連線資料庫－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 連線方法　使用者名稱/密碼/ 地址和埠號

# mysql 要  %s



conn = pymssql.connect(
    host='dbs.dev.sis.ai',
    user='sa',
    password='Mssql!@#123',
    database="Doris_test"

 )

cursor = conn.cursor()
def setSqlInsertion(path,table_name):
    try:
        with open(path, newline=''):

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
            cursor.executemany(sql_insert, rows)
            conn.commit()
    except Exception as e:
        print(e)

def setSqlSelection():
    query_sql='select * from Doris_test.dbo.qaTest9'
    query_results = cursor.execute(query_sql)
    # cursor.execute('select * from customers')
    # for results in query_results:
    print(cursor.execute(query_sql))
    conn.commit()

path = 'data003.csv'
table_name='qatest1'

setSqlInsertion(path,table_name)
# setSqlSelection()

cursor.close()