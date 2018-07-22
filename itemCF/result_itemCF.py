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

result = {}
for test_user in user_answer_test.keys():
    answers = user_answer_test[test_user]
    # temp_dic = similarity[test_user]
    # temp_dic = dict(sorted(temp_dic.items(), key=lambda x: x[1], reverse=True)) # sorted之后变为列表
    # 遍历用户test_user看过的每个答案
    for answer in answers.keys():
        similar_answers = similarity[answer]
        count = 0
        for simi_answer in similar_answers.keys():
            if simi_answer not in answers and simi_answer not in result.get(test_user, {}).keys():
                temp_dic = result.get(test_user, {})
                temp_dic[simi_answer] = similar_answers[simi_answer]*answers[answer]
                result[test_user] = temp_dic
        if len(result[test_user].keys()) > 400:
            break

for test_user in result.keys():
    temp_dic = result[test_user]
    temp = {}
    for answer in temp_dic.keys():
        ans = str(answer)[0:4]+str(answer)[-4:]
        if ans not in temp.keys():
            temp[ans] = temp_dic[answer]
    temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True)) # sorted之后变为列表
    result[test_user] = temp

import csv
w = csv.writer(open("D:\\CCIR2018\\result.csv", "w", newline='', encoding='utf-8'))
test = pd.read_table('D:\\CCIR2018\\newdata\\updated_testing_set_135089.txt\\testing_set_135089.txt', header=None)
print(test.iloc[:, 0].size)
for row in range(0, test.iloc[:, 0].size):
    userid = test.iloc[row, 0]
    answers = list(result.get(userid, {}).keys())[0:100]
    fill = 100 - len(answers)
    list1 = [-1 for i in range(fill)]
    answers.extend(list1)
    # temp = ','.join(answers)
    w.writerow(answers)

print("result字典大小："+str(len(result)))
print("推荐结果已生成！！！")

