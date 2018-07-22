import pandas as pd
import numpy as np
import pickle


# 保存每个用户的相似用户数
number_similar_item = 20

ftest = open('D:\\CCIR2018\\itemCF\\answer_user_test.txt', 'rb')
answer_user_test = pickle.load(ftest)
ftrain = open('D:\\CCIR2018\\itemCF\\answer_user_train.txt', 'rb')
answer_user_train = pickle.load(ftrain)

ftest.close()
ftrain.close()

# pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\answer_id.dict', header=None)
# candidate_df = pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\candidate.txt', header=None)
# candidate = {}
# for row in range(0, candidate_df.iloc[:, 0].size):
#     candidate[candidate_df.iloc[row, 1]] = 1

print(len(answer_user_test))

import time
# 用字典保存相似答案
similarity = {}
for test_user in answer_user_test.keys():
    # print(test_user)
    start = time.clock()
    answer1 = set(answer_user_test[test_user])
    if len(answer1) == 0:
        continue
    for train_user in answer_user_train.keys():
        answer2 = set(answer_user_train[train_user])
        intersect = answer1.intersection(answer2)
        len1 = len(intersect)
        simi = len1/(len(answer1)+len(answer2)-len1)
        if simi == 0:
            continue
        if(len(similarity.get(test_user, {})) < number_similar_item):
            temp_dic = similarity.get(test_user, {})
            temp_dic[train_user] = simi
            similarity[test_user] = temp_dic
        else:
            temp_dic = similarity[test_user]
            temp_dic = dict(sorted(temp_dic.items(), key=lambda x: x[1]))
            min_similarity = temp_dic[list(temp_dic.keys())[0]]
            if simi > min_similarity
                del temp_dic[list(temp_dic.keys())[0]]
                temp_dic[train_user] = simi
                similarity[test_user] = temp_dic
    print(time.clock() - start)

f = open('D:\\CCIR2018\\itemCF\\item_similarity_matrix.txt', 'wb')
pickle.dump(similarity, f)
f.close()


print(len(similarity))
print("相似答案已生成！！！")

