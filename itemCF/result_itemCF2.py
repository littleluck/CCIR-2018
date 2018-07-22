import pandas as pd
import numpy as np
import pickle


# 遍历user_answer_test.txt为每个用户推荐答案
ftest = open('D:\\CCIR2018\\itemCF\\user_answer_test.txt', 'rb')
user_answer_test = pickle.load(ftest)
ftrain = open('D:\\CCIR2018\\itemCF\\user_answer_train.txt', 'rb')
user_answer_train = pickle.load(ftrain)
fuser = open('D:\\CCIR2018\\itemCF\\test_user.txt', 'rb')
# test_user为集合
test_user = pickle.load(fuser)

fsimilarity = open('D:\\CCIR2018\\itemCF\\item_similarity_matrix2.txt', 'rb')
similarity = pickle.load(fsimilarity)

ftest.close()
ftrain.close()
fuser.close()
fsimilarity.close()

ftop100_answers = open('D:\\CCIR2018\\itemCF\\top100_answers.txt', 'rb')
top100_answers = pickle.load(ftop100_answers)
ftop100_answers.close()

import time

# print(len(user_answer_train))
# print(len(user_answer_test))

for user in test_user:
    if user not in user_answer_test and user in user_answer_train:
        user_answer_test[user] = user_answer_train[user]



result = {}
for test_user, watched_answers in user_answer_test.items():
    start = time.clock()
    # if len(watched_answers) == 0:
    #     print('--------------------')
    for answer, reading_time in watched_answers.items():
        for related_answer, simi in similarity.get(answer, {}).items():
            if related_answer in watched_answers:
                continue
            result.setdefault(test_user, {})
            result[test_user].setdefault(related_answer, 0)
            result[test_user][related_answer] += simi*float(reading_time)
        # if len(result.get(test_user, {})) > 100:
        #     break
    print(time.clock() - start)

print("----------------------")

for test_user, recommend_answers in result.items():
    temp = {}
    for answer, w in recommend_answers.items():
        ans = str(answer)[0:4]+str(answer)[-4:]
        if ans not in temp:
            temp[ans] = w
    temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True)[0:100])
    result[test_user] = temp

import csv
w = csv.writer(open("D:\\CCIR2018\\result.csv", "w", newline='', encoding='utf-8'))
test = pd.read_table('D:\\CCIR2018\\newdata\\updated_testing_set_135089.txt\\testing_set_135089.txt', header=None)
print(test.iloc[:, 0].size)
for row in range(0, test.iloc[:, 0].size):
    userid = test.iloc[row, 0]
    answers = list(result.get(userid, {}).keys())
    len1 = 100 - len(answers)
    temp_list = list(top100_answers.keys())
    i = 0
    j = 0
    while i < len1:
        if temp_list[j] in answers:
            j += 1
        else:
            answers.append(temp_list[j])
            i += 1

    # temp_list = list(top100_answers.keys())[0:100 - len(answers)]
    # answers.extend(temp_list)
    # fill = 100 - len(answers)
    # list1 = [-1 for i in range(fill)]
    # answers.extend(list1)
    # temp = ','.join(answers)
    w.writerow(answers)

print(len(user_answer_test))
print("result字典大小："+str(len(result)))
print("推荐结果已生成！！！")

