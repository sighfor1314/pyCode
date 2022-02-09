import csv

path = 'data001.csv'

with open(path, newline='') as csvfile:
    myCsvDic = csv.DictReader(csvfile)
    for row in myCsvDic:
        print (row)
        for key in row.keys():
            print(row[key])

# with open(path, newline='') as csvfile:
#     rows = csv.reader(csvfile)
#
#     headers = next(rows)
#     print('headers: %s' % headers)
#     array = list(rows)
#     # print(array)
#     for row in array:
#         print(row[0])
    # ss=",".join(headers)
    # sql = "insert into qaTest (id) values ('%s'),(row)"
    # print(ss)
#
# with open('data001.csv') as f:
#     myCsvDic = csv.DictReader(f)
#     array = list(myCsvDic)
#     length = len(array[0])
#     print(length)
#     # for dic in array:
#     #     for key in dic.keys():
#     #         print(dic[key])
#
    # cur.execute("INSERT INTO qaTest (id,c_char, c_char1) VALUES  ('%s')", (row[0], row[1], row[2]))