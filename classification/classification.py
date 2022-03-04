import pandas as pd
import shutil
import os
from os import walk
from os.path import join
import numpy as np


df = pd.read_excel("實習名額總表.xlsx")
df["企業名稱"] = df["企業名稱"].astype("category")
train_data = np.array(df)#np.ndarray()
train_x_list=train_data.tolist()#list
print(train_x_list[1])


for v in range(len(train_x_list)):

    MyPath = './'  # 當下目錄
    KeyWord = str(train_x_list[v])
    print(KeyWord[2:-2])
    companyName=KeyWord[2:-2]

    for root, dirs, files in walk(MyPath):
        for i in files:
            FullPath = join(root, i)  # 獲取檔案完整路徑
            FileName = join(i)  # 獲取檔案名稱

            if companyName in FullPath:
                if not os.path.exists(MyPath + '/' + companyName + '/' + FileName):
                    if not os.path.exists(companyName):
                        os.mkdir(companyName)
                    shutil.move(FullPath, MyPath + '/' + companyName)
                    print('成功將', FileName, '移動至', companyName, '資料夾')
                else:
                    print(FileName, '已存在，故不執行動作')
