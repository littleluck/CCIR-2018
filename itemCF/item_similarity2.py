import pandas as pd
import numpy as np
import pickle


# 保存每个用户的相似用户数
number_similar_item = 20

ftest = open('D:\\CCIR2018\\itemCF\\user_answer_train.txt', 'rb')   # 直接在user_answer_train.txt中建立答案相似性
user_answer_train = pickle.load(ftest)
ftrain = open('D:\\CCIR2018\\itemCF\\answer_user_train.txt', 'rb')
answer_user_train = pickle.load(ftrain)

ftest.close()
ftrain.close()


print(len(user_answer_train))

import math
import time
# 用字典保存相似答案
similarity = {}
for user, answers in user_answer_train.items():
    start = time.clock()
    list1 = list(answers.keys())
    len1 = len(list1)
    for i in range(0, len1):
        for j in range(i+1, len1):
            # print(type(list1))
            a = list1[i]
            b = list1[j]
            if a < b:
                similarity.setdefault(list1[i], {})
                similarity[list1[i]].setdefault(list1[j], 0)
                similarity[list1[i]][list1[j]] += 1
            else:
                similarity.setdefault(list1[j], {})
                similarity[list1[j]].setdefault(list1[i], 0)
                similarity[list1[j]][list1[i]] += 1
    print(time.clock() - start)

for answer1, related_answers in similarity.items():
    for answer2, count in related_answers.items():
        similarity[answer1][answer2] = count/math.sqrt(len(answer_user_train[answer1])*len(answer_user_train[answer2]))



f = open('D:\\CCIR2018\\itemCF\\item_similarity_matrix.txt', 'wb')
pickle.dump(similarity, f)
f.close()


print(len(similarity))
print("相似答案已生成！！！")

