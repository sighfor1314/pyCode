import mysql.connector

mydb = mysql.connector.connect(

  host="dbs.dev.sis.ai",
  user="root",
  password="jarvix123",
  database="db"
)

mycursor = mydb.cursor()
#
#
# # # #mycursor.execute("Drop DATABASE Doris_test01")
mycursor.execute("CREATE TABLE test008 ( id int,c_char VARCHAR(255), c_char1 VARCHAR(255),n_int int,b_boolean bit,t_time Date)")

mydb.commit()



# import pymssql
# conn = pymssql.connect(
#     host='dbs.dev.sis.ai',
#     user='sa',
#     password='Mssql!@#123',
#     database="Doris_test"
#
#  )
#
#
# # mscursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # conn.commit()
#
#
# cursor = conn.cursor()
# # cursor .execute("CREATE TABLE qatest3 (id VARCHAR(255), c_char VARCHAR(255))")
# # conn.commit()
# sql = "INSERT INTO qatest2 (id, c_char) VALUES (%s, %s)"
# val = ("8", 'NULL')
# cursor.execute(sql,val)
# conn.commit()
#
# #
# cursor.execute('select * from customers')
# #用一個rs變數獲取資料
# rs = cursor.fetchall()
# print(rs)

# # mscursor.execute("DROP TABLE IF EXISTS customers")
# # conn.commit()
# # # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# # # mycursor.execute("DROP TABLE IF EXISTS customerss")
# # # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# # # val = ("John1322", "Highway12 23332")
# # # mycursor.execute(sql, val)
# #
# # # mydb.commit()
# #
# # print(mycursor.rowcount, "record inserted.")
# #
#
# #
# # sql="select top 10 * from [dbo].[tblA]"
# #
# # cursor.execute(sql)
# # row = cursor.fetchone()
# # while row:
# # 	print(str(row[0])+" "+str(row[1])+" "+str(row[2]))
# # 	row = cursor.fetchone()
# # conn.close()
#
#
#