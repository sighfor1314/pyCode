import csv
import random
import time
#279.99mb 2045000
# 280.00 +2

taipei=['Songshan District','XinyiDistrict','Daan District','ZhongshanDistrict','ZhongzhengDistrict','Datong District','Wanhua District','Wenshan District','Nangang District','Neihu District','ShilinDistrict','Beitou District']
taipei_chinese=['松山區','信義區','大安區', '中山區','中正區','大同區', '萬華區', '文山區','南港區', '內湖區','士林區', '北投區'
]
newTaipei=['BanqiaoDistrict','SanchongDistrict','ZhongheDistrict','YongheDistrict','XinzhuangDistrict','XindianDistrict','TuchengDistrict','LuzhouDistrict','XizhiDistrict','ShulinDistrict','TamsuiDistrict ','YinggeDistrict','SanxiaDistrict',
           'RuifangDistrict','WuguDistrict','TaishanDistrict','LinkouDistrict','ShenkengDistrict','ShidingDistrict','PinglinDistrict','SanzhiDistrict','ShimenDistrict','BaliDistrict','PingxiDistrict','ShuangxiDistrict',
           'GongliaoDistrict','JinshanDistrict','WanliDistrict','WulaiDistrict'
           ]
newTaipei_chinese=['板橋區','三重區','中和區', '永和區', '新莊區', '新店區', '土城區', '蘆洲區','汐止區','樹林區','淡水區','鶯歌區','瑞芳區','五股區','泰山區','林口區','深坑區','石碇區','坪林區','三芝區','石門區','八里區','平溪區', '雙溪區','貢寮區', '金山區','萬里區', '烏來區']
taoyuan=['TaoyuanDistrict','ZhongliDistrict','DaxiDistrict','YangmeiDistrict','LuzhuDistrict','DayuanDistrict','GuishanDistrict','BadeDistrict','LongtanDistrict','PingzhenDistrict','XinwuDistrict','GuanyinDistrict','FuxingDistrict']
taoyuan_chinese=['桃園區','中壢區','大溪區','楊梅區','蘆竹區','大園區','龜山區','八德區','龍潭區','平鎮區','新屋區','觀音區','復興區']

bool=['true','false']

# t_time="%s%s%s"%(random.randint(1986,2050),random.randint(1,12),random.randint(1,12))
path = 'data0021.csv' # output FileName
a1=(2002,1,1,0,0,0,0,0,0) #設置開始日期時間元組（1976-01-01 00：00：00）
a2=(2002,12,31,23,59,59,0,0,0) #設置結束日期時間元組（1990-12-31 23：59：59）

start=time.mktime(a1) #生成開始時間戳
end=time.mktime(a2) #生成結束時間戳

#隨機生成10個日期字符串




with open(path, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(
    #     ['id', 'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13',
    #      'c14', 'c15'])
    # writer.writerow(
    #     ['id', 'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15',
    #      'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13',
    #      'c14', 'c15'])

    # writer.writerow([
    #      'id',
    #      'Taipei', '台北市', 'NewTaipei', '新北市','taoyuan','桃園市' ,
    #      'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10','n11', 'n12', 'n13', 'n14', 'n15',
    #      'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13','c14', 'c15'
    #      ]
    # )



    writer.writerow([  #寫標頭
         'id','c_char', 'c_char1','n_int','b_boolean','t_time'])




    # 10905650 --> 230.
    # 10905600 --> 230.00Gb
    # 10905500 --> 229.99Gb
    # 10905650 --> 230.01Gb


    for i in range(5):
        t = random.randint(start, end)  # 在開始和結束時間戳中隨機取出一個
        date_touple = time.localtime(t)  # 將時間戳生成時間元組
        date = time.strftime("%Y-%m-%d", date_touple)  # 將時間元組轉成格式化字符串（1976-05-21）
        # date+=" 00:00:00"
        writer.writerow([
            '',
            # taipei[random.randint(0,11)],
            # taipei_chinese[random.randint(0,11)],
            #
            # newTaipei[random.randint(0, 19)],
            # newTaipei_chinese[random.randint(0, 19)],
            #
            # taoyuan[random.randint(0, 12)],
            # taoyuan_chinese[random.randint(0, 12)],

            # random.randint(1, 200000),  # 0
            # random.randint(1, 200000),  # 1
            # random.randint(1, 200000),  # 2
            # random.randint(1, 200000),  # 3
            # random.randint(1, 200000),  # 4
            # random.randint(1, 200000),  # 5
            # random.randint(1, 200000),  # 6
            # random.randint(1, 200000),  # 7
            # random.randint(1, 200000),  # 8
            # random.randint(1, 200000),  # 9
            # random.randint(1, 200000),  # 10
            # random.randint(1, 200000),  # 11
            # random.randint(1, 200000),  # 12
            # random.randint(1, 200000),  # 13
            # random.randint(1, 200000),  # 14
            # random.randint(1, 200000),  # 15
            chr(random.randint(65, 90)),  # 0
            chr(random.randint(97, 122)),  # 1
            # chr(random.randint(97, 122)),  # 2
            # chr(random.randint(65, 90)),  # 3
            # chr(random.randint(97, 122)),  # 4
            # chr(random.randint(65, 90)),  # 5
            # chr(random.randint(97, 122)),  # 6
            # chr(random.randint(97, 122)),  # 7
            # chr(random.randint(65, 90)),  # 8
            # chr(random.randint(97, 122)),  # 9
            # chr(random.randint(65, 90)),# 10
            # chr(random.randint(97, 122)),  # 11
            # chr(random.randint(97, 122)),  # 12
            # chr(random.randint(65, 90)),  # 13
            # chr(random.randint(97, 122)),  # 14
            # chr(random.randint(65, 90))  # 15
            random.randint(1, 200000),
            random.randint(0,1),
            date



        ])
