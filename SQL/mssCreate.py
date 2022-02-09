import pymssql

conn = pymssql.connect(
    host='dbs.dev.sis.ai',
    user='sa',
    password='Mssql!@#123',
    database="Doris_test"

 )

cursor = conn.cursor()
#
#
# cursor.execute("Drop DATABASE Doris_test01")  # 待測試
# cursor.execute("DROP TABLE IF EXISTS qaTest1") #ok

'''
    msssql 沒有支援boolean boolean-->BIT 
'''
cursor.execute("CREATE TABLE test008 ( id int, c_char VARCHAR(255), c_char1 VARCHAR(255),n_int int,b_boolean BIT,t_time Date)") #ok


conn.commit()



# cursor.execute("SHOW DATABASES") # 待測試
# for x in cursor:
#   print(x)

# cursor.execute("SHOW Tables") # 待測試
# for x in cursor:
#   print(x)
