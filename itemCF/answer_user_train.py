import pandas as pd
import numpy as np
import pickle

# 这里train_answers.txt保存的是一个集合
fanswer = open('D:\\CCIR2018\\itemCF\\train_answers.txt', 'rb')
train_answers = pickle.load(fanswer)
ftrain = open('D:\\CCIR2018\\itemCF\\user_answer_train.txt', 'rb')
user_answer_train = pickle.load(ftrain)

fanswer.close()
ftrain.close()

import time
print(len(train_answers))
answer_user_train = {}
for answer in train_answers:
    start = time.clock()
    for train_user in user_answer_train.keys():
        temp_dic = user_answer_train[train_user]
        if answer in temp_dic.keys():
            answer_user_train.setdefault(answer, []).append(train_user)
    print(time.clock() - start)

f = open('D:\\CCIR2018\\itemCF\\answer_user_train.txt', 'wb')
pickle.dump(answer_user_train, f)
f.close()

print(len(answer_user_train))
print("answer_user_train.txt字典已生成！！！")

