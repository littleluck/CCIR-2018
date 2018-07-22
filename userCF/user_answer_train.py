import pandas as pd
import numpy as np
import pickle

# 用户阅读记录阈值
number_reading_answer = 30

dic = {}
for count in range(1, 26):
    train = pd.read_table('D:\\CCIR2018\\data_part\\training_'+str(count)+'txt', header=None)
    for row in range(0, train.iloc[:,0].size):
        dic.setdefault(train.iloc[row, 0], []).append(train.iloc[row, 1])

dic2 = {}
for train_user in dic.keys():
    answer = dic[train_user]
    if len(answer) >= number_reading_answer:
        dic2[train_user] = answer

f = open('D:\\CCIR2018\\user_answer_train.txt', 'wb')
pickle.dump(dic2, f)
f.close()

print(len(dic2))
print("user_answer_train.txt字典已生成！！！")





