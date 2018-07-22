import pandas as pd
import numpy as np
import pickle
# import sys

# 在每个相似的用户中取推荐答案的数量
number_similar_answer = 10

ftest = open('D:\\CCIR2018\\user_answer_test.txt', 'rb')
user_answer_test = pickle.load(ftest)
ftrain = open('D:\\CCIR2018\\user_answer_train.txt', 'rb')
user_answer_train = pickle.load(ftrain)

fsimilarity = open('D:\\CCIR2018\\user_similarity_matrix.txt', 'rb')
similarity = pickle.load(fsimilarity)

result = {}
for test_user in similarity.keys():
    answer1 = user_answer_test[test_user]
    temp_dic = similarity[test_user]
    temp_dic = dict(sorted(temp_dic.items(), key=lambda x: x[1], reverse=True)) # sorted之后变为列表
    for train_user in temp_dic.keys():
        answer2 = user_answer_train[train_user]
        temp_answer = list(set(answer2).difference(set(answer1)))   # answer1与answer2的差集
        temp_answer = list(set(temp_answer).difference(set(result.get(test_user, [])))) # 从temp_answer中减去已准备推荐给test_user的答案
        count = 0
        for answer in temp_answer:
            ans = str(answer)[0:4]+str(answer)[-4:]
            result.setdefault(test_user, []).append(ans)
            count += 1
            if count == number_similar_answer:
                break
        number_similar_answer = 10 + (number_similar_answer - count)


ftest.close()
ftrain.close()
fsimilarity.close()

import csv
w = csv.writer(open("D:\\CCIR2018\\result.csv", "w", newline='', encoding='utf-8'))
test = pd.read_table('D:\\CCIR2018\\newdata\\updated_testing_set_135089.txt\\testing_set_135089.txt', header=None)
print(test.iloc[:, 0].size)
for row in range(0, test.iloc[:, 0].size):
    userid = test.iloc[row, 0]
    answers = result.get(userid, [])
    # print(answers)
    # if len(answers) == 0:
    #     temp = user_answer_train.get(userid, [])[0:100]
    #     # print([str(x)[0:4]+str(x)[-4:] for x in temp])
    #     answers.extend([str(x)[0:4]+str(x)[-4:] for x in temp])
    fill = 100 - len(answers)
    list1 = [-1 for i in range(fill)]
    answers.extend(list1)
    # temp = ','.join(answers)
    w.writerow(answers)

print("result字典大小："+str(len(result)))
print("推荐结果已生成！！！")

