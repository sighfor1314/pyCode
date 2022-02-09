import cx_Oracle
import csv
import pandas as pd
cx_Oracle.init_oracle_client(lib_dir="/Users/synergies/Downloads/instantclient_19_8")

#　－－－－－連線資料庫－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 連線方法　使用者名稱/密碼/ 地址和埠號



conn = cx_Oracle.connect("system", "oracle", "192.168.66.107:1522/xe")
cur = conn.cursor()


def setSqlDeletion(table_name,count):
    for i in range(0,count):
        cur.execute("DELETE FROM %s Where id = %s " % (table_name,str(i)))


def setSqlInsertion(path,table_name):
    try:
        with open(path, newline=''):

            data = pd.read_csv(path)

            column_length = len(data.values[0])
            column_count = ""
            for i in range(1, column_length + 1):
                column_count += ':' + str(i)
                if i != column_length:
                    column_count += ','


            rows = [tuple(x) for x in data.values]
            sql_insert = "INSERT INTO %s VALUES (%s)" % (table_name, column_count)
            cur.executemany(sql_insert, rows)
            conn.commit()
    except Exception as e:
        print(e)

def setSqlSelection(table_name,table_column='*'):
    query_results = cur.execute("select %s FROM %s " %(table_column,table_name))
    for results in query_results:
        print(results)
# setSqlDeletion('qaTest2',200)
path = 'data003.csv'
table_name='qaTest3'
setSqlInsertion(path,table_name)

conn.commit()
cur.close()