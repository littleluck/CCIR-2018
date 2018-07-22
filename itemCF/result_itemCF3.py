import pandas as pd
import numpy as np
import pickle


# 遍历user_answer_test.txt为每个用户推荐答案
ftest = open('D:\\CCIR2018\\itemCF\\user_answer_test.txt', 'rb')
user_answer_test = pickle.load(ftest)

fsimilarity = open('D:\\CCIR2018\\itemCF\\item_similarity_matrix.txt', 'rb')
similarity = pickle.load(fsimilarity)

ftest.close()
fsimilarity.close()

# 取相似问题数
K = 20

print(len(user_answer_test))

import time

result = {}
for test_user, watched_answers in user_answer_test.items():
    start = time.clock()
    for answer, reading_time in watched_answers.items():
        for related_answer, simi in sorted(similarity[answer].items(), key=lambda x: x[1], reverse=True)[:K]:
            if related_answer in watched_answers:
                continue
            result.setdefault(test_user, {})
            result[test_user].setdefault(related_answer, 0)
            result[test_user][related_answer] += simi*float(reading_time)
        if len(result[test_user]) > 400:
            break
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
    fill = 100 - len(answers)
    list1 = [-1 for i in range(fill)]
    answers.extend(list1)
    # temp = ','.join(answers)
    w.writerow(answers)

print("result字典大小："+str(len(result)))
print("推荐结果已生成！！！")

