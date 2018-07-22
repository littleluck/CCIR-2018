import pandas as pd
import numpy as np
import pickle
# import sys

# 创建一个二维矩阵保存用户之间的相似性
# user_number = 7000000
# similarity_matrix = np.zeros((1000000, user_number))

# 保存每个用户的相似用户数
number_similar_user = 10

ftest = open('D:\\CCIR2018\\user_answer_test.txt', 'rb')
user_answer_test = pickle.load(ftest)
ftrain = open('D:\\CCIR2018\\user_answer_train.txt', 'rb')
user_answer_train = pickle.load(ftrain)
# fuser_index = open('D:\\CCIR2018\\user_index.txt', 'rb')
# user_index = pickle.load(fuser_index)

ftest.close()
ftrain.close()
# fuser_index.close()

# import time
# 用字典保存相似用户
similarity = {}
for test_user in user_answer_test.keys():
    # print(test_user)
    # start = time.clock()
    answer1 = set(user_answer_test[test_user])
    if len(answer1) == 0:
        continue
    for train_user in user_answer_train.keys():
        answer2 = set(user_answer_train[train_user])
        intersect = answer1.intersection(answer2)
        simi = len(intersect)/(len(answer1)+len(answer2)-len(intersect))
        if simi == 0:
            continue
        # index1 = user_index[test_user]
        # index2 = user_index[train_user]
        if(len(similarity.get(test_user, {})) < number_similar_user):
            temp_dic = similarity.get(test_user, {})
            temp_dic[train_user] = simi
            similarity[test_user] = temp_dic
        else:
            temp_dic = similarity[test_user]
            temp_dic = dict(sorted(temp_dic.items(), key=lambda x: x[1]))
            min_similarity = temp_dic[list(temp_dic.keys())[0]]
            if simi > min_similarity:
                del temp_dic[list(temp_dic.keys())[0]]
                temp_dic[train_user] = simi
                similarity[test_user] = temp_dic
    # print(time.clock() - start)

f = open('D:\\CCIR2018\\user_similarity_matrix.txt', 'wb')
pickle.dump(similarity, f)
f.close()


# np.savetxt("D:\\CCIR2018\\user_similarity_matrix.txt", similarity_matrix)
# 读取此相似度矩阵时，用matrix = numpy.loadtxt("filename.txt")

print(len(similarity))
print("相似用户已生成！！！")

